# View com Django

Esse repositório existe para eu estudar como criar views com 
templates no Django, servir arquivos estáticos e entender a 
página de Django Admin.

## Processo

1. Criar projeto

```{bash}
django-admin startproject djanguinho
cd djanguinho
python manage.py startapp core
```

2. Criei o modelo Note dentro de djanguinho/models.py

3. Criei os modelos dentro de core/template/

3. Criei o css dentro de core/static

4. Configurei as urls

3. Criei notas com o Django Admin

4. Acessei via web usando /notes/

## Build

Rodando...

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate
python3 manage.py runserver
```
