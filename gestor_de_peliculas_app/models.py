from django.db import models

# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_estreno = models.IntegerField()

    def __str__(self):
        return self.titulo


class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    peliculas = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
