from django.db import models
from django.utils import timezone

# Create your models here.

class Palet(models.Model):
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)
    dataCriacao = models.DateField(null=False, blank=False, default=timezone.now)
    ativo = models.BooleanField(null=False, blank=False, default=True)
    quantidadeItens = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return str(self.codigoBarras)

class Produto (models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False, unique=False)

    def __str__(self):
        return str(self.nome)

class Caixa (models.Model):
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)
    dataFabricacao = models.DateField(null=False, blank=False, default=timezone.now)
    dataSaide = models.DateField(null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    palet = models.ForeignKey(Palet, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigoBarras)

class Armazem(models.Model):
    nomeArmazem = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.nomeArmazem)

class Setor(models.Model):
    nomeSetor = models.CharField(max_length=50, null=False, blank=False)
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)
    dataCriacao = models.DateField(null=False, blank=False, default=timezone.now)
    ativo = models.BooleanField(blank=False, default=True)
    armazem = models.ForeignKey(Armazem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nomeSetor)

class PaletSetor(models.Model):
    palet = models.ForeignKey(Palet, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    dataInicoAlocacao = models.DateField(null=False, blank=False, default=timezone.now)
    dataFimAlocacao = models.DateField(null=True, blank=True)

