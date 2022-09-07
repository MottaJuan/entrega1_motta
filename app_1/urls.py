from django.urls import path
from app_1 import views

urlpatterns = [
    path('', views.inicio, name="inicio"),

    #path('entregables/', views.entregables, name="entregables"),
    # URLs de Equios
    path('equipos/', views.equipos, name="equipos"),

    # URLs de Entrenadores
    path('entrenadores/', views.entrenadores, name="entrenadores"),
  
    # URLs de Jugadores
     path('jugadores/', views.jugadores, name="jugadores"),
]