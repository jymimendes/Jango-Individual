from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artista', views.lista_artista, name='lista-artistas'),
    path('artista/cria', views.cria_artista, name='cria-artista'),
    path('artista/edita/<int:id>', views.edita_artista, name='edita-artista'),
    path('artista/remove/<int:id>', views.remove_artista, name='remove-artista'),
    path('musicas', views.lista_musicas, name='lista-musicas'),
    path('musicas/cria', views.cria_musica, name='cria-musica'),
    path('musicas/edita/<int:id>', views.edita_musica, name='edita-musica'),
    path('musicas/remove/<int:id>', views.remove_musica, name='remove-musica'),
]