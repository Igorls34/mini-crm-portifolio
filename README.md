# Mini CRM

Um sistema de CRM simples desenvolvido em Django seguindo as melhores práticas de desenvolvimento profissional.

## Funcionalidades

- **Autenticação Segura**: Login, logout e registro com proteção CSRF
- **Dashboard Moderno**: Cards com estatísticas e gráfico Chart.js
- **CRUD Completo de Leads**: Criar, listar, visualizar, editar e excluir
- **Busca e Filtros**: Busca por nome/email, filtro por status, ordenação
- **Paginação**: Lista de leads com paginação eficiente
- **Interface Responsiva**: Bootstrap 5 com design profissional
- **Interações Dinâmicas**: HTMX para melhor UX
- **Mensagens de Feedback**: Sistema de mensagens com ícones
- **Validação Completa**: Forms validados no backend
- **Arquitetura Limpa**: Separação de responsabilidades, código modular

## Tecnologias

- **Backend**: Django 5+ com Python 3.13+
- **Frontend**: Bootstrap 5, Font Awesome, HTMX, Chart.js
- **Banco**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Testes**: Faker para dados de teste

## Instalação e Configuração

### 1. Clonagem e Ambiente Virtual
```bash
git clone <url-do-repo>
cd mini-crm
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Configuração do Banco
```bash
python manage.py migrate
python manage.py createsuperuser  # Opcional
```

### 3. Dados de Teste
```bash
python manage.py seed_leads --qtd 50
```

### 4. Executar Servidor
```bash
python manage.py runserver
```

Acesse: http://127.0.0.0.1:8000/

## Estrutura do Projeto

```
crm_project/
├── crm_project/           # Configurações do projeto
│   ├── settings.py       # Configurações Django
│   ├── urls.py          # URLs principais
│   └── wsgi.py          # WSGI
├── leads/                # App principal
│   ├── models.py        # Modelo Lead
│   ├── views.py         # Views (funções)
│   ├── forms.py         # Formulários
│   ├── urls.py          # URLs do app
│   ├── apps.py          # Configuração do app
│   └── management/      # Comandos customizados
├── templates/           # Templates HTML
│   ├── base.html        # Template base
│   ├── includes/        # Componentes reutilizáveis
│   ├── dashboard.html   # Dashboard
│   ├── login.html       # Login
│   ├── register.html    # Registro
│   └── leads/           # Templates do app
├── static/              # Arquivos estáticos
│   ├── css/style.css    # Estilos customizados
│   └── js/              # JavaScript
├── db.sqlite3           # Banco de dados
├── manage.py            # Script de gerenciamento
└── requirements.txt     # Dependências
```

## Uso

1. **Acesse o sistema** e faça login ou registre-se
2. **Dashboard**: Visualize estatísticas gerais
3. **Gerenciar Leads**:
   - Criar novos leads
   - Buscar e filtrar leads existentes
   - Editar informações
   - Visualizar detalhes
   - Excluir quando necessário

## Desenvolvimento

### Padrões Seguidos

- **Arquitetura MTV**: Models, Templates, Views
- **Separação de Responsabilidades**: Views simples, lógica em models/forms
- **DRY (Don't Repeat Yourself)**: Templates reutilizáveis, includes
- **Segurança**: CSRF ativo, validação de dados, proteção XSS
- **Performance**: Consultas otimizadas, paginação
- **Manutenibilidade**: Código comentado, nomes descritivos

### Comandos Úteis

```bash
# Verificar código
python manage.py check

# Executar testes
python manage.py test

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Coletar arquivos estáticos (produção)
python manage.py collectstatic
```

## Produção

Para deploy em produção:

1. Configure variáveis de ambiente
2. Use PostgreSQL como banco
3. Configure `DEBUG = False`
4. Defina `ALLOWED_HOSTS`
5. Use servidor WSGI (Gunicorn)
6. Configure HTTPS
7. Use `collectstatic`

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto é open source e está sob a licença MIT.