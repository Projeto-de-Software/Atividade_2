import time

from django.forms import ModelForm
from django import forms
from .models import *
from .helpers import *

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'nome' : ('Nome:'),
            'codigoInterno' : ('Código'),
            'embalagem' : ('Embalagem'),
            'codigoBarras' : ('Código de Barras'),
            'quantidadeCaixa' : ('Quantidade por Caixa')
        }
        #help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'nome': {
                'max_length': ("O nome digitado é muito longo"),
                'blank': ('Não é possível adicionar um produto sem seu nome'),
                'null': ('Não é possível adicionar um produto sem seu nome')
            },
        }

class EntradaPalet(ModelForm):
    class Meta:
        model = SuperPalet
        fields = ('codigoBarras', 'produto', 'tipoEmbalagem' ,'quantidadeItens' , 'paleteria')
        labels = {
            'codigoBarras': ('Pallet:'),
            'quantidadeItens': ('Quantidade de Caixas:'),
            'produto': ('Produto:'),
            'tipoEmbalagem': ('Embalagem:'),
            'paleteria': ('Paleteria:'),
        }
        # help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código digitado é muito longo"),
                'blank': ('Não é possível armazenar um pallet sem um código de barras'),
                'null': ('Não é possível armazenar um pallet sem um código de barras')
            },
            'quantidadeItens': {
                'blank': ('Não é possível armazenar um pallet sem a quantidade de caixas'),
                'null': ('Não é possível armazenar um pallet sem a quantidade de caixas')
            },
            'produto': {
                'blank': ('Não é possível armazenar um pallet sem informar o produto'),
                'null': ('Não é possível armazenar um pallet sem informar o produto')
            },
            'tipoEmbalagem': {
                'blank': ('Não é possível armazenar um pallet sem informar o tipo de embalagem'),
                'null': ('NNão é possível armazenar um pallet sem informar o tipo de embalagem')
            },
            'paleteria': {
                'blank': ('Não é possível armazenar um pallet sem informar a paleteira'),
                'null': ('Não é possível armazenar um pallet sem informar a paleteira')
            },
        }
        widgets = {
            'produto' : forms.Select(attrs={'class': 'form-control select-search'}),
        }

class SaidaPalet(ModelForm):
    class Meta:
        model = SuperPalet
        fields = ('codigoBarras', 'quantidadeItens', 'produto', 'tipoEmbalagem', 'paleteria', 'dataArmazenamento')
        labels = {
            'codigoBarras': ('Pallet:'),
            'quantidadeItens': ('Quantidade de Caixas:'),
            'produto': ('Produto:'),
            'tipoEmbalagem': ('Embalagem:'),
            'paleteria': ('Paleteria:'),
            'dataArmazenamento': ('Data de Fabricação')
        }
        # help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código digitado é muito longo"),
                'blank': ('Não é possível armazenar um pallet sem um código de barras'),
                'null': ('Não é possível armazenar um pallet sem um código de barras')
            },
            'quantidadeItens': {
                'blank': ('Não é possível armazenar um pallet sem a quantidade de caixas'),
                'null': ('Não é possível armazenar um pallet sem a quantidade de caixas')
            },
            'produto': {
                'blank': ('Não é possível armazenar um pallet sem informar o produto'),
                'null': ('Não é possível armazenar um pallet sem informar o produto')
            },
            'tipoEmbalagem': {
                'blank': ('Não é possível armazenar um pallet sem informar o tipo de embalagem'),
                'null': ('NNão é possível armazenar um palet sem informar o tipo de embalagem')
            },
            'paleteria': {
                'blank': ('Não é possível armazenar um pallet sem informar a paleteira'),
                'null': ('Não é possível armazenar um pallet sem informar a paleteira')
            },
            'dataArmazenamento': {
                'blank': ('Não é possível armazenar um pallet sem informar a paleteira'),
                'null': ('Não é possível armazenar um pallet sem informar a paleteira')
            }
        }
        widgets = {
            'produto' : forms.Select(attrs={'class': 'form-control select-search'}),
            'dataArmazenamento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'})
        }

class NotaFiscalForm(forms.Form):
    numero = forms.IntegerField(required=False, label="Nº Nota Fiscal: ", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    serie = forms.IntegerField(required=False, label="Série da Nota Fiscal: ", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    dataCriacao = forms.DateField(label="Data da Nota Fiscal: ", widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}))
    produto = forms.ChoiceField(label='Produto: ', choices=(), widget=forms.Select(attrs={'class': 'select-produto'}))
    quantidade = forms.IntegerField(required=False, label="Quantidade de Caixas: ", widget=forms.NumberInput(attrs={'class': 'form-control'}))

