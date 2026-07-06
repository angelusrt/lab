# Postgres com Django

Esse repositório existe para eu estudar a conexão do Postgres em 
um projeto Django e criar um modelo simples. 

## Processo

1. Criar projeto

```{bash}
django-admin startproject core djanguinho
docker compose exec web python manage.py startapp djangao
```

2. Configurei 'settings.py' com a conexão do banco

3. Criei um modelo de itens em 'djanguinho/djangao/models.py'

4. Criei 'djanguinho/djangao/admin.py' e registrei o modelo criado


## Diretório

- manage.py: A command-line utility that lets you interact with this Django project in various ways.
- core/: A directory that is the actual Python package for your project.
- core/settings.py: Settings/configuration for this Django project.
- core/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- core/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
- core/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.

## Build

Instalando...

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate
```

Você precisará criar um arquivo '.env' com as seguintes variáveis:

```{bash}
POSTGRES_DB=[DB]
POSTGRES_USER=[User]
POSTGRES_PASSWORD=[Password]
POSTGRES_HOST=[Host]
POSTGRES_PORT=5432
```

Rodando (sem docker)...

```{bash}
python3 manage.py runserver
```

Rodando (com docker)...

```{bash}
docker compose up -d --build

## Somente na primeira vez
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

## Outros

Checando banco postgres...

```{bash}
docker compose exec db psql -U [myuser] -d [myproject]
```

Migrando...

```{bash}
docker compose exec web python manage.py makemigrations djangao
docker compose exec web python manage.py migrate djangao
```
