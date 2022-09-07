from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import Template, Context, loader
from app_1.models import Jugador, Entrenador, Equipo

def probar(request):
    queryset=Equipo.objects.all()
    diccionario={'app_1':queryset}
    plantilla=loader.get_template('plantilla1.html')
    documento_html=plantilla.render(diccionario)

    return HttpResponse(documento_html)

def inicio(request):

    return render(request,'app_1/inicio.html')

def jugadores(request):

    return render(request,'app_1/jugadores.html')

def entrenadores(request):

    return render(request,'app_1/entrenadores.html')

def equipos(request):

    return render(request,'app_1/equipos.html')