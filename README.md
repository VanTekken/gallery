# Gallery app for Django.

Note: Tested on Django 2.2 only. To install a specific version of Django, do the following:
1. Uninstall your current version `sudo pip uninstall django`
2. Install version 2.2 specifically `sudo pip install django==2.2`

This project makes use of [ParticlesJS](https://github.com/VincentGarreau/particles.js/)

Dependencies:
+ Bootstrap4 `sudo python3 -m pip install django-bootstrap4`
+ particles-js - installed in STATIC_ROOT

*Add configuration step instruct users to point to gallery.urls from within the parent application.
*You may need to use Django shell to remove QuerySets and upload your own via the /admin portal

## Getting Started

>Assuming you are creating a new django project to test this app
```
C:\> django-admin startproject [site_name]
```
```
C:\> cd [site_name]
```
```
C:\> git clone https://github.com/vantekken/gallery
```

1. Open up [site_name]/urls.py and add the following:
```python
from django.urls import include
...
urlpatterns += [
    path('', include('gallery.urls')),
]
```
3. Go into your settings file ([site_name]/settings.py), add the gallery app and bootstrap to Installed_Apps:
```
INSTALLED_APPS = [
    ...
    'django-bootstrap4',
    'gallery.apps.GalleryConfig',
    ...
]
```
> Be sure to install django-boostrap using pip if you haven't already
### Make the database migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py makemigrations gallery
```
```
python manage.py migrate gallery
```
### Create a superuser
```
C:\> python manage.py createsuperuser
```
### Start Server
```
C:\> python manage.py runserver 8000
```
> Browse to http://127.0.0.1:8000/gallery/

## To-do
1. Add requirements.txt
2. Remove ParticlesJS from repo and install as a requirement
