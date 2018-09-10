"""helpdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from markdownx import urls as markdownx
from faq import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #기본 관리자 앱
    path('faq/', include('faq.urls')), #FAQ앱
    path('kakao/', include('kakao.urls')), #kakao
    path('chat/', include('chat.urls')), #kakao
    path('', views.home), #index 연결
    url(r'^markdownx/', include('markdownx.urls')), #markdownx 앱
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
