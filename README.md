# Mini CRM - Sistema Completo de Gestão de Leads

Um sistema de CRM profissional desenvolvido em Django com interface moderna e funcionalidades avançadas para gestão completa de leads e pipeline de vendas.

## 🚀 Funcionalidades Principais

### Autenticação e Autorização
- **Sistema de Login Seguro**: Autenticação completa com proteção CSRF
- **Controle de Acesso**: Grupos de usuários (Admin, Gestor, Atendente)
- **Permissões Granulares**: Controle de acesso baseado em roles

### Dashboard Executivo
- **Cards de Estatísticas**: Métricas em tempo real (total, novos, em progresso, convertidos)
- **Gráficos Interativos**: Chart.js com visualizações de status e origem
- **Interface Responsiva**: Design moderno com Bootstrap 5

### Gestão Completa de Leads
- **CRUD Completo**: Criar, listar, visualizar, editar e excluir leads
- **Campos Avançados**: Nome, telefone, email, curso, origem, prioridade, probabilidade, valor, observações
- **Validação Completa**: Forms validados no backend com mensagens de erro

### Pipeline Kanban
- **Visualização Kanban**: Pipeline visual com colunas por status
- **Drag & Drop**: Arrastar leads entre status com JavaScript
- **Atualização em Tempo Real**: Mudanças salvas automaticamente

### Busca e Filtros Avançados
- **Busca Inteligente**: Por nome, email ou curso de interesse
- **Filtros Múltiplos**: Status, origem, prioridade, atendente, probabilidade, data
- **Ordenação**: Por qualquer campo em ordem crescente/decrescente
- **Paginação**: Navegação eficiente em listas grandes

### Relatórios e Exportações
- **Exportação Excel**: Arquivo XLSX formatado profissionalmente
- **Exportação PDF**: Relatório em PDF com tabelas organizadas
- **Filtros Aplicados**: Respeita todos os filtros ativos na exportação

### Logs de Atividades
- **Auditoria Completa**: Registro de todas as ações dos usuários
- **Histórico Detalhado**: Data, usuário, ação e valores alterados
- **Filtros de Log**: Busca por usuário, ação, período

### API REST
- **Django REST Framework**: API completa para integração
- **Serializers**: Dados estruturados para consumo externo
- **Autenticação**: Tokens para acesso seguro

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 5.2.3**: Framework web robusto e escalável
- **Python 3.13.3**: Última versão com performance otimizada
- **SQLite**: Banco de dados para desenvolvimento
- **PostgreSQL**: Recomendado para produção

### Frontend
- **Bootstrap 5**: Framework CSS responsivo e moderno
- **Font Awesome**: Ícones vetoriais profissionais
- **HTMX**: Interações dinâmicas sem JavaScript complexo
- **Chart.js**: Gráficos interativos e responsivos

### Bibliotecas Python
- **ReportLab**: Geração de PDFs profissionais
- **OpenPyXL**: Manipulação de arquivos Excel
- **Pillow**: Processamento de imagens
- **Faker**: Dados de teste realistas

## 📋 Pré-requisitos

- Python 3.8+
- Pip (gerenciador de pacotes Python)
- Git (para versionamento)

## 🚀 Instalação e Configuração

### 1. Clonagem do Repositório
```bash
git clone https://github.com/Igorls34/mini-crm-portifolio.git
cd mini-crm-portifolio
```

### 2. Ambiente Virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

### 3. Dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração do Banco
```bash
python manage.py migrate
python manage.py create_groups
```

### 5. Criar Superusuário (Opcional)
```bash
python manage.py createsuperuser
```

### 6. Dados de Teste
```bash
python manage.py seed_leads --qtd 50
```

### 7. Executar Servidor
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

## 👥 Usuários de Teste

Após executar `create_groups`, estarão disponíveis:

- **Admin**: admin / admin123 (acesso total)
- **Gestor**: gestor / gestor123 (gestão de leads)
- **Atendente**: atendente / atendente123 (leads próprios)

## 📊 Estrutura do Projeto

```
mini-crm/
├── crm_project/          # Configurações Django
├── leads/               # App principal
│   ├── migrations/      # Migrações do banco
│   ├── management/      # Comandos customizados
│   ├── templates/       # Templates HTML
│   └── static/          # CSS, JS, imagens
├── static/              # Arquivos estáticos coletados
├── templates/           # Templates base
├── db.sqlite3          # Banco de dados (não versionado)
└── manage.py           # Script de gerenciamento Django
```

## 🔧 Comandos Úteis

```bash
# Criar grupos de usuários
python manage.py create_groups

# Popular banco com dados de teste
python manage.py seed_leads --qtd 100

# Coletar arquivos estáticos
python manage.py collectstatic

# Executar testes
python manage.py test

# Verificar configurações
python manage.py check
```

## 🌐 URLs Principais

- `/` - Dashboard
- `/leads/` - Lista de leads
- `/leads/pipeline/` - Pipeline Kanban
- `/leads/activity-logs/` - Logs de atividades
- `/leads/export/xlsx/` - Exportar para Excel
- `/leads/export/pdf/` - Exportar para PDF
- `/api/` - API REST

## 📈 Funcionalidades Avançadas

### Pipeline Kanban
- Interface visual intuitiva
- Drag & drop entre colunas
- Atualização automática de status
- Logs de mudança de status

### Sistema de Permissões
- **Admin**: Acesso total ao sistema
- **Gestor**: Gestão de todos os leads
- **Atendente**: Apenas leads próprios

### Exportações Inteligentes
- Respeitam filtros aplicados
- Formatação profissional
- Dados completos incluindo observações

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Igor Silva** - [GitHub](https://github.com/Igorls34)

---

⭐ **Dê uma estrela se este projeto te ajudou!**

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