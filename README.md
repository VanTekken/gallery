# Gallery app for the Django framework.

So you're gonna need Django (obviously), particles-js in your STATIC_ROOT, and configure your URLS.conf file to include gallery.urls. 
Currently only works in a Django dev environment.
You may need to use Django shell to remove QuerySets and upload your own via the /admin portal :)

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
urlpatterns += [
    path('gallery/', include('gallery.urls')),
]
```
2. Open up gallery/admin.py and add:
```python 
admin.site.register(FileUpload)
```
3. Go into your settings file ([site_name]/settings.py) and add the gallery app to Installed_Apps:
```
INSTALLED_APPS = [
    ...
    'gallery.apps.GalleryConfig',
    ...
]
```

 
