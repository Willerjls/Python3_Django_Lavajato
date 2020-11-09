from django.contrib import admin
from lavajato.models import Veiculo, Cliente, Venda


class Veiculos(admin.ModelAdmin):
    list_display = ('id', 'placa', 'ano', 'modelo', 'descricao')
    list_display_links = ('id', 'placa')
    search_fields = ('placa',)


admin.site.register(Veiculo, Veiculos)


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Cliente, Clientes)


class Vendas(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'veiculo')
    list_display_links = ('id',)


admin.site.register(Venda, Vendas)
