from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
	path('', views.index),
]

if settings.DEBUG:
	urlpatterns += [
		re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
		#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	]
	urlpatterns += [
		re_path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
		#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
		path(r'^ajax/desc/$', views.desc, name='desc'),
	]