# API com Django

Estudando autênticação e API com Django.

## Deps

> [Saber mais sobre allauth](https://docs.allauth.org/en/latest/)

## Processo

- Rodei `django-admin startproject core .`
- Rodei `python3 manage.py startapp djanguinho`
- Configurar core/settings.py (installed_apps, templates, etc)
- Configurei o OAuth

## OAuth

- Ir no 'console.cloud.google.com/apis/credentials'
- Criar a tela de consentimento
- Adicionar URI: http://127.0.0.1:8000/accounts/google/login/callback/
- Registrar o JSON e o Client_ID pela página Admin do Django

## Build

Instalando...

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Rodando...

```{bash}
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Configurando usuário...

```{bash}
python manage.py shell
```

```{python}
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

bi_user = User.objects.create_user(username='bi_service', password=None)
bi_user.is_active = True
bi_user.save()

token = Token.objects.create(user=bi_user)
print(token.key)  # cola esse valor na config do BI
```

Rodando testes...

```{bash}
python manage.py test
```
