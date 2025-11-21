from django.core.management.base import BaseCommand
from faker import Faker
from leads.models import Lead
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Gera leads falsos para testes'

    def add_arguments(self, parser):
        parser.add_argument('--qtd', type=int, default=50, help='Quantidade de leads a gerar')

    def handle(self, *args, **options):
        fake = Faker('pt_BR')
        qtd = options['qtd']

        # Garantir que há usuários
        if not User.objects.exists():
            User.objects.create_user(username='admin', password='admin123')

        users = list(User.objects.all())

        cursos = [
            'Engenharia de Software',
            'Administração',
            'Medicina',
            'Direito',
            'Psicologia',
            'Arquitetura',
            'Marketing',
            'Contabilidade',
        ]

        for _ in range(qtd):
            Lead.objects.create(
                nome=fake.name(),
                telefone=fake.phone_number(),
                email=fake.email(),
                curso_interesse=random.choice(cursos),
                status=random.choice([choice[0] for choice in Lead.STATUS_CHOICES]),
                atendente=random.choice(users) if users else None,
                observacoes=fake.text(max_nb_chars=200) if random.choice([True, False]) else '',
            )

        self.stdout.write(self.style.SUCCESS(f'{qtd} leads criados com sucesso!'))