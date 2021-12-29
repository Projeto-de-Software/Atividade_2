from django.db import models
from django.utils import timezone

# Create your models here.
TIPO_EMBALAGEM = (
    ('GARRAFA', 'GARRAFA'),
    ('UNIDADE', 'UNIDADE'),
    ('BANDEJA','BANDEJA'),
    ('BALDE','BALDE'),
    ('LITRO','LITRO'),
    ('QUILOGRAMA','QUILOGRAMA'),
)

STATUS = (
    ('ABERTA', 'ABERTA'),
    ('CONFERIDA', 'CONFERIDA'),
    ('FINALIZADA','FINALIZADA'),
)

class Produto (models.Model):
    codigoInterno = models.IntegerField(null=False, blank=False, default=0)
    nome = models.CharField(max_length=120, blank=False, null=False, unique=False)
    embalagem = models.CharField(choices=TIPO_EMBALAGEM, null=False, blank=False, max_length=20, default='UNIDADE')
    codigoBarras = models.CharField(max_length=20, blank=False, null=False, unique=True)
    quantidadeCaixa = models.IntegerField(null=False, blank=False, default=1)


    def __str__(self):
        return str(self.codigoBarras) + " - " + str(self.nome)


TIPO_CAIXA = (
    ('PA', 'PAPELÃO'),
    ('PL', 'PLÁSTICO')
)

class SuperPalet(models.Model):
    codigoBarras = models.CharField(max_length=40, blank=False, null=False)
    dataArmazenamento = models.DateField(null=False, blank=False, default=timezone.now)
    dataRetirada = models.DateField(null=True, blank=True)
    quantidadeItens = models.IntegerField(blank=False, null=False, default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipoEmbalagem = models.CharField(max_length=2, choices=TIPO_CAIXA, default='PA', blank=False, null=False)
    paleteria = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.codigoBarras)

class NotaFiscal (models.Model):
    numero = models.IntegerField(null=False, blank=False)
    serie = models.IntegerField(null=True, blank=True)
    dataCriacao = models.DateField(null=False, blank=False, default=timezone.now)
    status = models.CharField(choices=STATUS, null=False, blank=False, max_length=20, default='ABERTA')

    def __str__(self):
        return str(self.numero)


class NotaFiscalProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    notaFiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)




