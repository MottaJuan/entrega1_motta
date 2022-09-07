from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from app_1.models import Jugador, Entrenador, Equipo

def probar(request):
    queryset=Equipo.objects.all()
    diccionario={'app_1':queryset}
    plantilla=loader.get_template('plantilla1.html')
    documento_html=plantilla.render(diccionario)

    return HttpResponse(documento_html)