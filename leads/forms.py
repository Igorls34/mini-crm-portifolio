from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Filtrar atendente apenas para usuários que podem atribuir
        if self.user and not self.user.groups.filter(name__in=['ADMIN', 'GESTOR']).exists():
            # ATENDENTE só pode ver a si mesmo
            self.fields['atendente'].queryset = self.fields['atendente'].queryset.filter(pk=self.user.pk)
            # Remover campo observacao_interna
            if 'observacao_interna' in self.fields:
                del self.fields['observacao_interna']

    class Meta:
        model = Lead
        fields = ['nome', 'telefone', 'email', 'curso_interesse', 'status', 'atendente', 'origem', 'valor_curso', 'prioridade', 'probabilidade_fechamento', 'data_proximo_contato', 'observacoes', 'observacao_interna']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'id': 'telefone', 'placeholder': '(11) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'curso_interesse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Curso de interesse'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'atendente': forms.Select(attrs={'class': 'form-select'}),
            'origem': forms.Select(attrs={'class': 'form-select'}),
            'valor_curso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'probabilidade_fechamento': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '100', 'placeholder': '0-100'}),
            'data_proximo_contato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações adicionais'}),
            'observacao_interna': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Observações internas (apenas para gestores/admins)'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'curso_interesse': 'Curso de Interesse',
            'status': 'Status',
            'atendente': 'Atendente',
            'origem': 'Origem do Lead',
            'valor_curso': 'Valor do Curso',
            'prioridade': 'Prioridade',
            'probabilidade_fechamento': 'Probabilidade de Fechamento (%)',
            'data_proximo_contato': 'Data do Próximo Contato',
            'observacoes': 'Observações',
            'observacao_interna': 'Observação Interna',
        }