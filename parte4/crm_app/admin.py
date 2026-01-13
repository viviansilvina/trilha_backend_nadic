from django.contrib import admin
from .models import *

admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Contato)
admin.site.register(Oportunidade)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(VendaProduto)
