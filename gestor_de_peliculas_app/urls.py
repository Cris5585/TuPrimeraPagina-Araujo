from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crear-pelicula/', views.crear_pelicula, name='crear_pelicula'),
    path('crear-director/', views.crear_director, name='crear_director'),
    path('crear-actor/', views.crear_actor, name='crear_actor'),
    path('buscar/', views.buscar_peliculas, name='buscar_peliculas'),

    # Vistas basadas en clases
    path('crear-serie/', views.SerieCreateView.as_view(), name='crear_serie'),
    path('listar-series/', views.SerieListView.as_view(), name='listar_series'),
    path('detalle-series/<int:pk>/',
          views.SerieDetailView.as_view(), name='detalle_series'),
    path('editar/<int:pk>/', views.SerieUpdateView.as_view(), name='editar_serie'),
    path('eliminar/<int:pk>/', views.SerieDeleteView.as_view(), name='eliminar_serie'),
 
]
