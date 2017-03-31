"""schistoprot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^help$', views.manual, name='help'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^surface_app$', views.surface_app, name='surface_app'),
    url(r'^secretory_app$', views.secretory_app, name='secretory_app'),
    url(r'^surface$', views.surface, name='surface'),
    url(r'^secretory$', views.secretory, name='secretory'),
    url(r'^surface_progress/(?P<task_id>[A-Za-z0-9-]+)$', views.surface_progress, name='surface_progress'),
    url(r'^secretory_progress/(?P<task_id>[A-Za-z0-9-]+)$', views.secretory_progress, name='secretory_progress'),
    url(r'^surface_results/(?P<task_id>[A-Za-z0-9-]+)$', views.surface_results, name='surface_results'),
    url(r'^secretory_results/(?P<task_id>[A-Za-z0-9-]+)$', views.secretory_results, name='secretory_results'),
]
