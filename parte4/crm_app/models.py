from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome   

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_vendida = models.IntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
   
    def save(self, *args, **kwargs):
        if self.produto.quantidade_estoque< self.quantidade_vendida:
            raise ValueError("Quantidade vendida maior que a quantidade em estoque.")
        self.valor_total = self.produto.preco * self.quantidade_vendida
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade_vendida} de {self.produto.nome} em {self.data_venda}"
    
