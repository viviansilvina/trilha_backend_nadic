from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    faturamento_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='clientes', default=None)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contatos')
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Oportunidade(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('ganha', 'Ganha'),
        ('perdida', 'Perdida'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='oportunidades')
    descricao = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Oportunidade {self.id}"


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    oportunidade = models.OneToOneField(Oportunidade, on_delete=models.CASCADE, related_name='venda', default=None)
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.id}"


class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.produto.quantidade_estoque < self.quantidade:
            raise ValueError("Estoque insuficiente")

        self.subtotal = self.produto.preco * self.quantidade

        if self.produto.quantidade_estoque >= self.quantidade:
            self.produto.quantidade_estoque -= self.quantidade
            self.produto.save()

            super().save(*args, **kwargs)

            self.venda.valor_final += self.subtotal
            self.venda.save()

            empresa = self.venda.oportunidade.cliente.empresa
            empresa.faturamento_total += self.subtotal
            empresa.save()
