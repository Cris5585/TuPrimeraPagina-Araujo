from django import forms
from .models import Pelicula, Director, Actor

class PeliculaForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    director = forms.CharField() 
    genero = forms.CharField(max_length=50)
    fecha_estreno = forms.IntegerField()


class DirectorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)

    

class ActorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    peliculas = forms.CharField(max_length=100)