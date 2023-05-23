from django.contrib import admin
from .models import Categoria, Cliente, Locacao, Filme

@admin.register(Categoria)
class Admincategoria(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Cliente)
class Admincliente(admin.ModelAdmin):
    list_display = ('nome','email',)

@admin.register(Filme)
class Adminfilme(admin.ModelAdmin):
    list_display = ('titulo','valor',)

@admin.register(Locacao)
class Adminregister(admin.ModelAdmin):
    list_display = ('nome','data',)