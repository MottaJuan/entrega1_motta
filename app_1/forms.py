from django import forms

class EquipoFormulario(forms.Form):
    nombre=forms.CharField(max_length=60)
    categoria=forms.CharField(max_length=60)
    liga=forms.CharField(max_length=60)

class JugadorFormulario(forms.Form):
    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    fecha_nacimiento=forms.DateField()
    num_camiseta=forms.IntegerField()
    email=forms.EmailField()

class EntrenadorFormulario(forms.Form):
    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    fecha_nacimiento=forms.DateField()
    email=forms.EmailField()