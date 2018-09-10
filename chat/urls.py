from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('room', views.room, name='room'),
]
