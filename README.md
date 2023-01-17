# library-catalog

Django API for Library Management System

### Installation and Setup:

You first need an env ☘️

```python
# create the env
conda create --name libraryenv

# install requirements
pip install -r requirements.txt
```

This project uses PostgreSQL. If you wish to use another database you would need to modify "DATABASES" in settings.py
accordingly. Otherwise you just need a .env file with DB credentials.
Migrate models to your db

```python
python manage.py migrate
```

Start the app

```python
python manage.py runserver
```

### Documentation 📝:

Complete docs of the API are available at the endpoint:

```
http://{HOST}/docs
```
