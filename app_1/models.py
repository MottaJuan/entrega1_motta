from __future__ import division
from msilib.schema import Class
from django.db import models

class Jugador(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=64)
    fecha_nacimiento=models.DateField()
    num_camiseta=models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Entrenador(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=64)
    fecha_nacimiento=models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Equipo(models.Model):
    nombre=models.CharField(max_length=128)
    categoria=models.CharField(max_length=128)
    liga=models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.nombre}'