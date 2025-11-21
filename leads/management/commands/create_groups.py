from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from leads.models import Lead

class Command(BaseCommand):
    help = 'Cria grupos de usuários e permissões para o CRM'

    def handle(self, *args, **options):
        # Criar grupos
        admin_group, created = Group.objects.get_or_create(name='ADMIN')
        gestor_group, created = Group.objects.get_or_create(name='GESTOR')
        atendente_group, created = Group.objects.get_or_create(name='ATENDENTE')

        # Obter content type do Lead
        lead_content_type = ContentType.objects.get_for_model(Lead)

        # Permissões básicas
        view_lead = Permission.objects.get(content_type=lead_content_type, codename='view_lead')
        add_lead = Permission.objects.get(content_type=lead_content_type, codename='add_lead')
        change_lead = Permission.objects.get(content_type=lead_content_type, codename='change_lead')
        delete_lead = Permission.objects.get(content_type=lead_content_type, codename='delete_lead')

        # Atribuir permissões
        # ATENDENTE: ver e editar apenas leads próprios
        atendente_group.permissions.add(view_lead, add_lead, change_lead)

        # GESTOR: tudo exceto deletar usuários
        gestor_group.permissions.add(view_lead, add_lead, change_lead, delete_lead)

        # ADMIN: tudo
        admin_group.permissions.add(view_lead, add_lead, change_lead, delete_lead)

        self.stdout.write(self.style.SUCCESS('Grupos e permissões criados com sucesso!'))