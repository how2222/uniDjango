# Project Description
### Goal
A webapp for trading projections 
### Caracteristics
- A dashboard with market summary
- A projection generator for each stock
### Stacks :
Python, javascript, html, css
Django

# Project setup
## Django
### Creating a virtual environment for the project to tackle depedencies
- ```python -m venv env```
- ```source env/bin/activate   # on Linux/Mac```
### Installing Django
```pip install django```
### Creating a Django project
```django-admin startproject umessage```
### Starting the project
```python manage.py runserver```
### Create an app in the Django project
- ```python manage.py startapp exampleApp```
- Modify : umessage/settings.py
```python
INSTALLED_APPS = [
    ...
    'exampleApp',
]
```
## Dependencies
### Installing Tailwind-css
```pip install django-tailwind```
doc : https://django-tailwind.readthedocs.io/en/latest/installation.html
### Launching Tailwind-css
```python manage.py tailwind start```
### Library for icons
lucide.dev
### Yahoo finance
pip install yfinance


# Project tips
## Change the name of an app
```mv past_name new_name```