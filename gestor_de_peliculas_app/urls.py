from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-pelicula/', views.crear_pelicula, name='crear_pelicula'),
    path('crear-director/', views.crear_director, name='crear_director'),
    path('crear-actor/', views.crear_actor, name='crear_actor'),
    path('buscar/', views.buscar_peliculas, name='buscar_peliculas'),
]
