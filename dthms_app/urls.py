from django.urls import path
from django.contrib import admin
from dthms_app import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login', views.login, name='login')
]