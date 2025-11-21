from rest_framework import serializers
from .models import Lead, ActivityLog


class LeadSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    origem_display = serializers.CharField(source='get_origem_display', read_only=True)
    prioridade_display = serializers.CharField(source='get_prioridade_display', read_only=True)
    atendente_nome = serializers.CharField(source='atendente.get_full_name', read_only=True)

    class Meta:
        model = Lead
        fields = [
            'id', 'nome', 'telefone', 'email', 'curso_interesse',
            'origem', 'origem_display', 'prioridade', 'prioridade_display',
            'probabilidade_fechamento', 'valor_curso', 'atendente',
            'atendente_nome', 'status', 'status_display',
            'data_criacao', 'data_proximo_contato', 'observacao_interna'
        ]
        read_only_fields = ['id', 'data_criacao']


class ActivityLogSerializer(serializers.ModelSerializer):
    lead_nome = serializers.CharField(source='lead.nome', read_only=True)
    user_nome = serializers.CharField(source='user.get_full_name', read_only=True)
    action_display = serializers.CharField(source='get_action_display', read_only=True)

    class Meta:
        model = ActivityLog
        fields = [
            'id', 'lead', 'lead_nome', 'user', 'user_nome',
            'action', 'action_display', 'old_value', 'new_value',
            'description', 'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']