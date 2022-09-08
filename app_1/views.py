from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import Template, Context, loader
from app_1.models import Jugador, Entrenador, Equipo
from app_1.forms import EquipoFormulario, JugadorFormulario, EntrenadorFormulario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


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
    equipos=Equipo.objects.all()
    return render(request,'app_1/equipos.html',{'equipos':equipos})

def crear_equipo(request):
    if request.method == 'POST':
        formulario = EquipoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            equipo =  Equipo(nombre=data['nombre'], categoria=data['categoria'], liga=data['liga'])
            equipo.save()
            return render(request, "app_1/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = EquipoFormulario()  # Formulario vacio para construir el html
    return render(request, "app_1/form_equipo.html", {"formulario": formulario})

def crear_jugador(request):
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            jugador =  Jugador(nombre=data['nombre'], apellido=data['apellido'], fecha_nacimiento=data['fecha_nacimiento'],num_camiseta=data['num_camiseta'],email=data['email'])
            jugador.save()
            return render(request, "app_1/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = JugadorFormulario()  
    return render(request, "app_1/form_jugador.html", {"formulario": formulario})

def crear_entrenador(request):
    if request.method == 'POST':
        formulario = EntrenadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            entrenador =  Entrenador(nombre=data['nombre'], apellido=data['apellido'], fecha_nacimiento=data['fecha_nacimiento'],email=data['email'])
            entrenador.save()
            return render(request, "app_1/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = EntrenadorFormulario()  
    return render(request, "app_1/form_entrenador.html", {"formulario": formulario})

 
def busqueda_equipos(request):
    return render(request, "app_1/form_busqueda_equipo.html")

def buscar_equipos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        equipos=Equipo.objects.filter(nombre__icontains=nombre)
        return render(request,'app_1/equipos.html',{'equipos':equipos})
    else:
        return render(request,'app_1/equipos.html',{'equipos':[]})