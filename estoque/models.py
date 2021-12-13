from django.db import models
from django.utils import timezone

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False, unique=False)
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)

    def __str__(self):
        return str(self.nome)


TIPO = (
    ('C','Caixa'),
    ('P', 'Palet'),
)

TIPO_CAIXA = (
    ('PA', 'Papelão'),
    ('PL', 'Plástico')
)

class TipoCaixa(models.Model):
    tipo = models.CharField(max_length=2, choices=TIPO, default='C', blank=False, null=False)
    tipoCaixa = models.CharField(max_length=2, choices=TIPO_CAIXA, default='PA' ,blank=False, null=False)
    quantidadeProdutosTipoCaixa = models.IntegerField(blank=False, null=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str("Caixa" if self.tipo == "C" else "Palet") + " - " + str("Papelão" if self.tipoCaixa == "PA" else "Plástico") + " - " + str(self.quantidadeProdutosTipoCaixa) + " - " + str(self.produto.nome)

class Palet(models.Model):
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)
    dataCriacao = models.DateField(null=False, blank=False, default=timezone.now)
    ativo = models.BooleanField(null=False, blank=False, default=True)
    quantidadeItens = models.IntegerField(blank=False, null=False, default=1)
    tipoCaixa = models.ForeignKey(TipoCaixa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigoBarras)


class Caixa (models.Model):
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)
    dataFabricacao = models.DateField(null=False, blank=False, default=timezone.now)
    dataSaide = models.DateField(null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    palet = models.ForeignKey(Palet, on_delete=models.CASCADE)
    tipoCaixa = models.ForeignKey(TipoCaixa, on_delete=models.CASCADE)
    quantidadeProdutosCaixa = models.IntegerField(blank=False, null=False)

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

class SetorLocalizacao(models.Model):
    coluna = models.IntegerField(null=False, blank=False)
    linha = models.IntegerField(null=False, blank=False)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

class PaletSetor(models.Model):
    palet = models.ForeignKey(Palet, on_delete=models.CASCADE)
    setorLocalizacao = models.ForeignKey(SetorLocalizacao, on_delete=models.CASCADE)
    dataInicoAlocacao = models.DateField(null=False, blank=False, default=timezone.now)
    dataFimAlocacao = models.DateField(null=True, blank=True)


