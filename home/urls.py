from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('produtos/', views.produtos, name="produtos"),
    path('produtos/formulario/', views.form_produtos, name="form_produtos"),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('diasemana/<int:id>/', views.diasemana, name='dia_semana'),
]