from django import forms

class EquipoFormulario(forms.Form):
    nombre=forms.CharField(max_length=60)
    categoria=forms.CharField(max_length=60)
    liga=forms.CharField(max_length=60)