# Project Description
## Goal
A webapp for uni student networks or alumni networks to discuss globally with all the community, but without the spam. 
## Caracteristics
- Classic messaging system
- User rotation to send messages, to avoid spam
- Limiting sending message to 1 message per month
## Stacks :
Python, Django

# Project setup
## Creating a virtual environment for the project to tackle depedencies
python -m venv env
source env/bin/activate   # on Linux/Mac
## Installing Django
pip install django
## Creating a Django project
django-admin startproject umessage
## Starting the project
python manage.py runserver
## Create an app in the Django project
- python manage.py startapp exampleApp
- Modify : umessage/settings.py
INSTALLED_APPS = [
    ...
    'exampleApp',
]
