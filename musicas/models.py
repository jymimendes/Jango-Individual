from django.db import models

# Create your models here.

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nome

class Musica(models.Model):
    nome = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="+")
    
    def __str__(self) -> str:
        return self.nome
    
