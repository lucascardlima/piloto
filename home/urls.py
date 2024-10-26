from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    
]