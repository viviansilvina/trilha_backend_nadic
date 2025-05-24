from django.contrib import admin
from .models import Produto, Cliente, Funcionario, Venda

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque')
    search_fields = ('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario', 'data_admissao')
    search_fields = ('nome', 'cargo')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade_vendida', 'data_venda', 'valor_total', 'cliente', 'vendedor')
    search_fields = ('produto__nome', 'cliente__nome')
    list_filter = ('data_venda',)