import time

from django.forms import ModelForm
from django import forms
from .models import *

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ('nm_produto', 'cd_interno', 'cd_barras', 'prazo_validade', 'qt_unid_cx_papelao', 'qt_unid_cx_plastico')
        labels = {
            'nm_produto': ('Nome: '),
            'cd_interno':('Código interno '),
            'cd_barras':('Código de barras: '),
            'prazo_validade':('Prazo de validade: '),
            'qt_unid_cx_papelao':('Quantidade de unidades na caixa de papelão: '),
            'qt_unid_cx_plastico':('Quantidade de unidades na caixa de plástico: ')
        }

class RuaForm(ModelForm):
    class Meta:
        model = Rua
        fields = ('nm_rua',)
        labels = {
            'nm_rua': ('Nome: '),
        }

class PaleteiraForm(ModelForm):
    class Meta:
        model = Paleteira
        fields = ('nr_paleteira','tp_paleteira', 'rua_id')
        labels = {
            'nr_paleteira': ('Número da paleteira: '),
            'tp_paleteira': ('Tipo da paleteira: '),
            'rua_id' : ('Rua: ')
        }
        widgets = {
            'rua_id': forms.Select(attrs={'class': 'select-search'}),
        }

    def __init__(self, *args, **kwargs):
        super(PaleteiraForm, self).__init__(*args, **kwargs)
        self.fields['rua_id'].queryset = Rua.objects.filter(sn_deletado=False, sn_ativo=True)

class BlocoForm(ModelForm):
    class Meta:
        model = Bloco
        fields = ('paleteira_id','cd_barras', 'cd_bloco', 'qt_fileiras_pallet')
        labels = {
            'paleteira_id': ('Paleteira: '),
            'cd_barras': ('Código de barras: '),
            'cd_bloco' : ('Código do Bloco: '),
            'qt_fileiras_pallet': ('Quantidade de fileiras: '),
        }
        widgets = {
            'paleteira_id': forms.Select(attrs={'class': 'select-search'}),
        }

    def __init__(self, *args, **kwargs):
        super(BlocoForm, self).__init__(*args, **kwargs)
        self.fields['paleteira_id'].queryset = Paleteira.objects.filter(sn_deletado=False, sn_ativo=True)

class RuaProdutoForm(forms.ModelForm):
    class Meta:
        model = RuaProduto
        fields = ('produto_id','rua_id')
        labels = {
            'produto_id': 'Produto',
            'rua_id': 'Rua'
        }
        widgets = {
            'produto_id': forms.Select(attrs={'class': 'select-search'}),
            'rua_id': forms.Select(attrs={'class': 'select-search disabled'})
        }

    def __init__(self, *args, **kwargs):
        super(RuaProdutoForm, self).__init__(*args, **kwargs)
        self.fields['produto_id'].queryset = Produto.objects.filter(sn_deletado=False, sn_ativo=True)
        self.fields['rua_id'].queryset = Rua.objects.filter(sn_deletado=False, sn_ativo=True)

class EntradaPalletForm(forms.ModelForm):
    class Meta:
        model = Pallet
        fields = ('produto_id', 'cd_barras', 'tp_embalagem', 'qt_unidade', 'sn_sobra')
        labels = {
            'produto_id': ('Produto: '),
            'cd_barras': ('Código de barras: '),
            'tp_embalagem': ('Tipo de embalagem: '),
            'qt_unidade': ('Quantidade de Unidades: '),
            'sn_sobra' : ('Sobra: ')
        }
        widgets = {
            'produto_id': forms.Select(attrs={'class': 'select-search disabled', }),
            'sn_sobra': forms.Select(attrs={'class': 'select-search'}),
            'tp_embalagem': forms.Select(attrs={'class': 'select-search'})
        }