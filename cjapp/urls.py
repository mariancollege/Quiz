"""cjapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from restapi.views import *
from restapi import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'', index),
    path('quiz', views.quiz, name='quiz'),
    path('addquestion/', views.addquestion, name='addquestion'),
    path('viewanswer/', views.view_answer, name='view_answer'),
    path('viewquestion/', views.view_quiz, name='view_quiz'),
    path('registration/', views.regis, name='regis'),
    path('', views.log, name='log'),
    path('login/', views.log, name='log'),
    path('score/', views.score, name='score'),
    path('addquiz/', views.add_quiz, name='addquiz'),
]
