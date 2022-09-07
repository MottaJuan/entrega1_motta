from __future__ import division
from msilib.schema import Class
from django.db import models

class Jugador(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=64)
    fecha_nacimiento=models.DateField()
    num_camiseta=models.IntegerField()
    email = models.EmailField()


class Entrenador(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=64)
    fecha_nacimiento=models.DateField()
    email = models.EmailField()

class Equipo(models.Model):
    nombre=models.CharField(max_length=128)
    categoria=models.CharField(max_length=128)
    liga=models.CharField(max_length=128)