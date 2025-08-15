from django.contrib import admin
from .models import Director, Pelicula, Actor

# Register your models here.
register_models = [Director, Pelicula, Actor]

admin.site.register(register_models)