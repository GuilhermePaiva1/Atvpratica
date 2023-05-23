from django.shortcuts import render
from .models import Locacao, Filme
# Create your views here.
def index(request):
    return render(request, 'index.html')

def locacao(request):
    lista = Locacao.objects.all() #pegando dados do banco.
    context={'locacoes': lista} #preparando os dados para o .html
    return render(request,'locacao.html',context)

def filmes(request):
    lista = Filme.objects.all() #pegando dados do banco.
    context={'filmes': lista} #preparando os dados para o .html
    return render(request,'filmes.html',context)