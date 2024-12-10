from django.shortcuts import render, redirect, get_object_or_404
from .models import Musica, Artista

# Create your views here.

def home(request):
    return render(request, 'home.html')


# Artistas

def lista_artista(request):
    artistas = Artista.objects.all()
    return render(request, 'lista_artista.html', {"artistas": artistas})

def cria_artista(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        nacionalidade = request.POST.get("nacionalidade")
        artista = Artista()
        artista.nome = nome
        artista.idade = idade
        artista.nacionalidade = nacionalidade
        artista.save()
        return redirect('lista-artistas')
    return render(request, 'form_artista.html')

def edita_artista(request, id):
    artista = get_object_or_404(Artista, pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        nacionalidade = request.POST.get("nacionalidade")
        artista.nome = nome
        artista.idade = idade
        artista.nacionalidade = nacionalidade
        artista.save()
        return redirect('lista-artistas')
    return render(request, 'form_artista.html', {"artista": artista})

def remove_artista(request, id):
    artista = get_object_or_404(Artista, pk=id)
    artista.delete()
    return redirect('lista-artistas')


# Musicas

def lista_musicas(request):
    musicas = Musica.objects.all()
    return render(request, 'lista_musica.html', {"musicas": musicas})


def cria_musica(request):
    artistas = Artista.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome")
        artista = request.POST.get("artista")
        musica = Musica()
        musica.nome = nome
        musica.artista = get_object_or_404(Artista, pk=artista)
        musica.save()
        return redirect('lista-musicas')
    return render(request, 'form_musica.html', {"artistas": artistas})

def edita_musica(request, id):
    artistas = Artista.objects.all()
    musica = get_object_or_404(Musica, pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        artista = request.POST.get("artista")
        musica.nome = nome
        musica.artista = get_object_or_404(Artista, pk=artista)
        musica.save()
        return redirect('lista-musicas')
    return render(request, 'form_musica.html', {"artistas": artistas, "musica": musica})

def remove_musica(request, id):
    musica = get_object_or_404(Musica, pk=id)
    musica.delete()
    return redirect('lista-musicas')
    