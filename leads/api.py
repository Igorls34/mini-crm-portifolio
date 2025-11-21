from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Lead, ActivityLog
from .serializers import LeadSerializer, ActivityLogSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Lead.objects.all()

        # Filtros por query parameters
        status = self.request.query_params.get('status', None)
        origem = self.request.query_params.get('origem', None)
        prioridade = self.request.query_params.get('prioridade', None)
        atendente = self.request.query_params.get('atendente', None)
        prob_min = self.request.query_params.get('prob_min', None)
        prob_max = self.request.query_params.get('prob_max', None)

        # Filtrar por permissões do usuário
        if self.request.user.groups.filter(name='ATENDENTE').exists():
            queryset = queryset.filter(atendente=self.request.user)

        if status:
            queryset = queryset.filter(status=status)
        if origem:
            queryset = queryset.filter(origem=origem)
        if prioridade:
            queryset = queryset.filter(prioridade=prioridade)
        if atendente:
            queryset = queryset.filter(atendente_id=atendente)
        if prob_min:
            queryset = queryset.filter(probabilidade_fechamento__gte=prob_min)
        if prob_max:
            queryset = queryset.filter(probabilidade_fechamento__lte=prob_max)

        return queryset

    def perform_create(self, serializer):
        lead = serializer.save()
        # Criar log de atividade
        ActivityLog.objects.create(
            lead=lead,
            user=self.request.user,
            action='created',
            description=f'Lead criado via API por {self.request.user.get_full_name() or self.request.user.username}'
        )

    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_status = old_instance.status
        old_atendente = old_instance.atendente

        lead = serializer.save()

        # Criar logs de atividade
        if old_status != lead.status:
            ActivityLog.objects.create(
                lead=lead,
                user=self.request.user,
                action='status_changed',
                old_value=old_status,
                new_value=lead.status,
                description=f'Status alterado via API'
            )

        if old_atendente != lead.atendente:
            ActivityLog.objects.create(
                lead=lead,
                user=self.request.user,
                action='assigned',
                old_value=str(old_atendente) if old_atendente else None,
                new_value=str(lead.atendente) if lead.atendente else None,
                description=f'Atendente alterado via API'
            )

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        lead = self.get_object()
        new_status = request.data.get('status')

        if request.user.groups.filter(name='ATENDENTE').exists() and lead.atendente != request.user:
            return Response({'error': 'Permissão negada'}, status=403)

        if new_status in dict(Lead.STATUS_CHOICES):
            old_status = lead.status
            lead.status = new_status
            lead.save()

            # Criar log
            ActivityLog.objects.create(
                lead=lead,
                user=request.user,
                action='status_changed',
                old_value=old_status,
                new_value=new_status,
                description=f'Status alterado via API'
            )

            return Response({'success': True})
        else:
            return Response({'error': 'Status inválido'}, status=400)


class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = ActivityLog.objects.select_related('lead', 'user')

        # Filtros
        lead = self.request.query_params.get('lead', None)
        user = self.request.query_params.get('user', None)
        action = self.request.query_params.get('action', None)

        # Filtrar por permissões
        if self.request.user.groups.filter(name='ATENDENTE').exists():
            queryset = queryset.filter(lead__atendente=self.request.user)

        if lead:
            queryset = queryset.filter(lead_id=lead)
        if user:
            queryset = queryset.filter(user_id=user)
        if action:
            queryset = queryset.filter(action=action)

        return queryset