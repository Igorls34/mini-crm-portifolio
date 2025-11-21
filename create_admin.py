#!/usr/bin/env python
import os
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')
django.setup()

from django.contrib.auth.models import User

# Remover todos os superusuários
superusers = User.objects.filter(is_superuser=True)
count = superusers.count()
superusers.delete()
print(f'Removidos {count} superusuários.')

# Criar superusuário padrão
username = 'admin'
email = 'admin@example.com'
password = 'admin123'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuário criado: {username} - Email: {email} - Senha: {password}')
else:
    print(f'Superusuário {username} já existe.')
    user = User.objects.get(username=username)
    user.set_password(password)
    user.email = email
    user.save()
    print(f'Senha e email atualizados para {username}.')