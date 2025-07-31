from django.shortcuts import render, redirect
from .forms import PeliculaForm, DirectorForm, ActorForm
from .models import Pelicula, Director, Actor
# Create your views here.

def home(request):
    return render(request, 'gestor_peliculas/home.html')

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            Pelicula.objects.create(
                titulo=form.cleaned_data['titulo'],
                director=form.cleaned_data['director'],
                genero=form.cleaned_data['genero'],
                fecha_estreno=form.cleaned_data['fecha_estreno']
            )
            return redirect('home')
    else:
        form = PeliculaForm()

    return render(request, 'gestor_peliculas/crear_pelicula.html', {'form': form})

def crear_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            Director.objects.create(
                nombre=form.cleaned_data['nombre'],
                pais=form.cleaned_data['pais']
            )
            return redirect('home')
    else:
        form = DirectorForm()
    return render(request, 'gestor_peliculas/crear_director.html', {'form': form})

def crear_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            Actor.objects.create(
                nombre=form.cleaned_data['nombre'],
                peliculas=form.cleaned_data['peliculas']
            )
            return redirect('home')
    else:
        form = ActorForm()
    return render(request, 'gestor_peliculas/crear_actor.html', {'form': form})

def buscar_peliculas(request):
    resultado = []
    if 'titulo' in request.GET:
        titulo = request.GET['titulo']
        resultado = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, 'gestor_peliculas/buscar.html', {'resultado': resultado})

