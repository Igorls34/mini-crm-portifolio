from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    STATUS_CHOICES = [
        ('novo', 'Novo'),
        ('contato', 'Em Contato'),
        ('progresso', 'Em Progresso'),
        ('convertido', 'Convertido'),
        ('perdido', 'Perdido'),
    ]

    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    curso_interesse = models.CharField(max_length=120, verbose_name="Curso de Interesse")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='novo',
        verbose_name="Status",
        db_index=True
    )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    atendente = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Atendente"
    )
    observacoes = models.TextField(blank=True, verbose_name="Observações")

    ORIGEM_CHOICES = [
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp'),
        ('facebook', 'Facebook'),
        ('indicacao', 'Indicação'),
        ('google', 'Google'),
        ('organico', 'Orgânico'),
        ('evento', 'Evento'),
    ]

    origem = models.CharField(
        max_length=20,
        choices=ORIGEM_CHOICES,
        default='organico',
        verbose_name="Origem do Lead"
    )

    valor_curso = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Valor do Curso"
    )

    data_proximo_contato = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do Próximo Contato"
    )

    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
        verbose_name="Prioridade"
    )

    probabilidade_fechamento = models.IntegerField(
        default=0,
        verbose_name="Probabilidade de Fechamento (%)",
        help_text="0-100"
    )

    observacao_interna = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observação Interna"
    )

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.nome} - {self.get_status_display()}"


class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('created', 'Lead Criado'),
        ('updated', 'Lead Atualizado'),
        ('status_changed', 'Status Alterado'),
        ('deleted', 'Lead Excluído'),
        ('assigned', 'Atendente Atribuído'),
    ]

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.lead}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Log de Atividade"
        verbose_name_plural = "Logs de Atividade"
