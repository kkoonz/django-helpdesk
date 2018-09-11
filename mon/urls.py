from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'mon'
urlpatterns = [
    path('', views.index),
    path('index', views.index),
]
