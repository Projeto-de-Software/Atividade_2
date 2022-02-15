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

TIPO_CAIXA = (
    ('PA', 'PAPELÃO'),
    ('PL', 'PLÁSTICO')
)

TP_PALETEIRA = (
    ('C', 'CORREDOR'),
    ('N', 'NORMAL')
)

TP_MOVIMENTACAO = (
    ('E', "Entrada"),
    ('S', "Saída")
)

class Produto(models.Model):
    nm_produto = models.CharField(max_length=500, blank=False, null=False)
    cd_interno = models.IntegerField(blank=False, null=False)
    cd_barras = models.CharField(max_length=20, blank=False, null=False)
    prazo_validade = models.IntegerField(blank=False, null=False) #Prazo de validade em dias
    qt_unid_cx_papelao = models.IntegerField(blank=False, null=False)
    qt_unid_cx_plastico = models.IntegerField(blank=False, null=False)
    sn_ativo = models.BooleanField(blank=False, null=False, default=True) #Validação atualização
    sn_deletado = models.BooleanField(blank=False, null=False, default=True) #Validação excliusão

class Pallet (models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cd_barras = models.CharField(max_length=20, blank=False, null=False)
    tp_embalagem = models.CharField(max_length=10, blank=False, null=False, choices=TIPO_EMBALAGEM)
    qt_unidade = models.IntegerField(blank=False, null=False)
    dt_fabricacao = models.DateField(auto_now=True, blank=False, null=False)
    sn_sobra = models.BooleanField(blank=False, null=False, default=False) #Validação de sobra de produção
    sn_armazenado = models.BooleanField(blank=False, null=False, default=True) #Validação de o pallet ainda estar no sistema

class Caixa(models.Model):
    pallet_id = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    qt_unidade = models.IntegerField(blank=False, null=False)
    sn_ativo = models.BooleanField(blank=False, null=False, default=True)

class Rua (models.Model):
    nm_rua = models.CharField(max_length=50, blank=False, null=False)
    sn_ativo = models.BooleanField(blank=False, null=False, default=True) #Validação atualização
    sn_deletado = models.BooleanField(blank=False, null=False, default=True) #Validação excliusão

class RuaProduto(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    rua_id = models.ForeignKey(Rua, on_delete=models.CASCADE)
    sn_ativo = models.BooleanField(blank=False, null=False, default=True) #Validação atualização
    sn_deletado = models.BooleanField(blank=False, null=False, default=True) #Validação excliusão

class Paleteira (models.Model):
    rua_id = models.ForeignKey(Rua, on_delete=models.CASCADE)
    nr_paleteira = models.IntegerField(blank=False, null=False)
    tp_paleteira = models.CharField(max_length=2, blank=False, null=False, choices=TP_PALETEIRA, default='N')
    sn_ativo = models.BooleanField(blank=False, null=False, default=True) #Validação atualização
    sn_deletado = models.BooleanField(blank=False, null=False, default=True) #Validação excliusão

class Bloco (models.Model):
    paleteira_id = models.ForeignKey(Paleteira,on_delete=models.CASCADE)
    cd_barras = models.CharField(max_length=20, blank=False, null=False)
    cd_bloco = models.CharField(max_length=3, blank=False, null=False)
    qt_fileiras_pallet = models.IntegerField(blank=False, null=False)
    sn_ativo = models.BooleanField(blank=False, null=False, default=True) #Validação atualização
    sn_deletado = models.BooleanField(blank=False, null=False, default=True) #Validação excliusão

class PalletBloco(models.Model):
    pallet_id = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    bloco_id = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    dt_entrada = models.DateField(auto_now=True, blank=False, null=False)
    dt_saida = models.DateField(auto_now=False, blank=True, null=True)

class MovPallet(models.Model):
    pallet_id = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    qt_unidade = models.IntegerField(blank=False, null=False)
    tp_movimentacao = models.CharField(max_length=10, blank=False, null=False, choices=TP_MOVIMENTACAO)
    dt_movimentacao = models.DateField(auto_now=True, blank=False, null=False)
