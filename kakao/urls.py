from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'kakao'
urlpatterns = [
    path('message', views.message, name='message'),
    path('keyboard/', views.keyboard, name='keyboard'),
]
