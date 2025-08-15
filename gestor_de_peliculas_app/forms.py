from django import forms
from .models import Pelicula, Director, Actor, Serie


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


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo', 'director', 'genero','fecha_estreno']