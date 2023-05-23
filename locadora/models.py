from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Locacao(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filme = models.ManyToManyField(Filme)
    
    def __srt__(self):
        return self.nome


