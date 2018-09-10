from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'faq'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:answer_id>/', views.detail, name='detail'),
]