from rest_framework import serializers
from .models import Empresa, Produto, Cliente, Venda, VendaProduto

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VendaProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaProduto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    itens = VendaProdutoSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'
