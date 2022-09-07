from django.urls import path
from app_1 import views

urlpatterns = [
    path('', views.inicio, name="inicio"),

    #path('entregables/', views.entregables, name="entregables"),
    # URLs de Equios
    path('equipos/', views.equipos, name="equipos"),
    path('crear-equipo/', views.crear_equipo, name="crear_equipo"),
    path('busqueda-equipo-form/',views.busqueda_equipos, name="busqueda_equipo_form"),
    path('busqueda-equipo/',views.buscar_equipos, name="busqueda_equipo"),
    # URLs de Entrenadores
    path('entrenadores/', views.entrenadores, name="entrenadores"),
  
    # URLs de Jugadores
     path('jugadores/', views.jugadores, name="jugadores"),
]