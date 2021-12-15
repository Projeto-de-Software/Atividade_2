import time

from django.forms import ModelForm
from django import forms
from .models import *
from .helpers import *

class ArmazenForm(ModelForm):
    class Meta:
        model = Armazem
        fields = '__all__'
        labels = {
            'nomeArmazem' : ('Nome:'),
        }
        #help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'nomeArmazem': {
                'max_length': ("O nome digitado é muito longo"),
                'blank': ('Não é possível adicionar um armazem sem seu nome'),
                'null': ('Não é possível adicionar um armazem sem seu nome')
            },
        }

class PaletForm(ModelForm):
    class Meta:
        model = Palet
        fields = ('codigoBarras', 'dataCriacao', 'quantidadeItens','tipoCaixa','produto')
        labels = {
            'codigoBarras': ('Código de barras: '),
            'dataCriacao': ('Data de Fabricação: '),
            'quantidadeItens': ('Quantidade de itens: '),
            'tipoCaixa': ('Regra: '),
            'produto' : ('Produto:')
        }
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código de barras digitado é muito longo"),
                'blank': ('Não é possível adicionar um palet sem o código de barras.'),
                'null': ('Não é possível adicionar um palet sem o código de barras.')
            },
            'dataCriacao': {
                'blank': ('Não é possível adicionar um palet sem a data de fabricação'),
                'null': ('Não é possível adicionar um palet sem a data de fabricação')
            },
            'quantidadeItens': {
                'blank': ('Não é possível adicionar um palet sem a quantidade de itens que ele armazena.'),
                'null': ('Não é possível adicionar um palet sem a quantidade de itens que ele armazena.')
            },
            'tipoCaixa' : {
                'blank': ('Não é possível adicionar um palet sem selecionar o tipo de caixa.'),
                'null': ('Não é possível adicionar um palet sem selecionar o tipo de caixa.')
            }
        }

        widgets = {
            'dataCriacao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'tipoCaixa' : forms.Select(attrs={'class':'form-contrl select-search'}),
            'produto': forms.Select(attrs={'class': 'form-contrl select-search'})
        }

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

class CaixaForm(ModelForm):
    class Meta:
        model = Caixa
        fields = ('codigoBarras', 'dataFabricacao', 'produto', 'palet','tipoCaixa', 'quantidadeProdutosCaixa')
        labels = {
            'codigoBarras': ('Código de barras: '),
            'dataFabricacao': ('Data de Fabricação: '),
            'produto': ('Produto: '),
            'palet': ('Código do palet: '),
            'tipoCaixa': ('Tipo da Caixa: '),
            'quantidadeProdutosCaixa': ('Quantidade de produtos:')
        }
        #help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código de barras digitado é muito longo"),
                'blank': ('Não é possível adicionar uma caixa sem o código de barras.'),
                'null': ('Não é possível adicionar uma caixa sem o código de barras.')
            },
            'dataFabricacao': {
                'blank': ('Não é possível adicionar uma caixa sem a data de fabricação'),
                'null': ('Não é possível adicionar uma caixa sem a data de fabricação')
            },
            'produto': {
                'blank': ('Não é possível adicionar uma caixa sem informar o produto.'),
                'null': ('Não é possível adicionar uma caixa sem informar o produto.')
            },
            'palet': {
                'blank': ('Não é possível adicionar uma caixa sem informar o código do palet.'),
                'null': ('Não é possível adicionar uma caixa sem informar o código do palet.')
            },
            'tipoCaixa': {
                'blank': ('Não é possível adicionar uma caixa sem informar o tipo de caixa.'),
                'null': ('Não é possível adicionar uma caixa sem informar o tipo de caixa.')
            }

        }
        widgets = {
            'dataFabricacao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'tipoCaixa' : forms.Select(attrs={'class': 'form-control select-search'}),
            'palet' : forms.Select(attrs={'class': 'form-control select-search'}),
            'produto' : forms.Select(attrs={'class': 'form-control select-search'}),
        }

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['nomeSetor', 'codigoBarras', 'dataCriacao', 'armazem']
        labels = {
            'codigoBarras': ('Código de barras: '),
            'nomeSetor': ('Nome do setor: '),
            'dataCriacao': ('Data de Criação: '),
            'armazem': ('Armazen: ')
        }
        #help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código de barras digitado é muito longo"),
                'blank': ('Não é possível adicionar uma caixa sem o código de barras.'),
                'null': ('Não é possível adicionar uma caixa sem o código de barras.')
            },
            'nomeSetor': {
                'blank': ('Não é possível adicionar um setor sem atribuir um nome.'),
                'null': ('Não é possível adicionar um setor sem atribuir um nome.')
            },
            'dataCriacao': {
                'blank': ('Não é possível adicionar um setor sem a data de criação'),
                'null': ('Não é possível adicionar um setor sem a data de criação')
            },
            'armazem': {
                'blank': ('Não é possível adicionar um setor sem informar um armazem'),
                'null': ('Não é possível adicionar um setor sem informar um armazem.')
            }

        }
        widgets = {
            'dataCriacao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'armazem': forms.Select(attrs={'class':'form-control select-search'})
        }

class CaixaSaidaForm(ModelForm):
    class Meta:
        model = Caixa
        fields = ('codigoBarras', 'dataFabricacao', 'dataSaide', 'palet','produto')
        labels = {
            'codigoBarras': ('Código de barras: '),
            'dataFabricacao': ('Data de Fabricação: '),
            'produto': ('Produto: '),
            'palet': ('Código do palet: '),
            'dataSaide': ('Data de Saída: ')
        }
        #help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código de barras digitado é muito longo"),
                'blank': ('Não é possível adicionar uma caixa sem o código de barras.'),
                'null': ('Não é possível adicionar uma caixa sem o código de barras.')
            },
            'dataFabricacao': {
                'blank': ('Não é possível adicionar uma caixa sem a data de fabricação'),
                'null': ('Não é possível adicionar uma caixa sem a data de fabricação')
            },
            'dataSaide':{
                'blank': ('Não é possível dar saída em uma caixa sem a data de saída'),
                'null': ('Não é possível dar saída em uma caixa sem a data de saída')
            },
            'produto': {
                'blank': ('Não é possível adicionar uma caixa sem informar o produto.'),
                'null': ('Não é possível adicionar uma caixa sem informar o produto.')
            },
            'palet': {
                'blank': ('Não é possível adicionar uma caixa sem informar o código do palet.'),
                'null': ('Não é possível adicionar uma caixa sem informar o código do palet.')
            }

        }
        widgets = {
            'dataFabricacao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date', 'disabled':True}),
            'dataSaide' : forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
            'codigoBarras': forms.TextInput(attrs={'disabled': True}),
            'produto': forms.Select(attrs={'disabled': True}),
            'palet': forms.Select(attrs={'disabled': True}),
        }

class SetorLocalizacaoForm(ModelForm):
    class Meta:
        model = SetorLocalizacao
        fields = '__all__'
        labels = {
            'coluna' : ('Quantidade de Secções:'),
            'linha': ('Quantidade de Prateleiras:'),
            'setor': ('Setor:')
        }
        error_messages = {
            'coluna': {
                'blank': ('Não é possível gerar as localizações sem informar a quantidade de secções.'),
                'null': ('Não é possível gerar as localizações sem informar a quantidade de secções.')
            },
            'linha': {
                'blank': ('Não é possível gerar as localizações sem informar a quantidade de prateleiras.'),
                'null': ('Não é possível gerar as localizações sem informar a quantidade de prateleiras.')
            },
        }
        widgets = {
            'setor': forms.Select(attrs={'disabled': True})
        }

class TipoCaixaForm(ModelForm):
    class Meta:
        model = TipoCaixa
        fields = '__all__'
        labels = {
            'tipo': ('Modo:'),
            'tipoCaixa': ('Tipo Caixa:'),
            'quantidadeProdutosTipoCaixa': ('Quantidade:'),
            'produto': ('Produto:')
        }

class EntradaPaletSetorForm(forms.Form):
    palet = forms.ChoiceField(label='Palet: ', choices=(), widget=forms.Select(attrs={'class':'select-palet'}))
    setor = forms.ChoiceField(label='Setor: ', choices=(), widget=forms.Select(attrs={'class':'select-setor'}))
    setorLocalizacao = forms.ChoiceField(label='Localizacão: ', choices=(), widget=forms.Select(attrs={'class':'select-setor-localizacao'}))
    dataInicoAlocacao = forms.DateField(label="Data Alocação" ,widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}))

class SaidaPaletSetorForm(forms.Form):
    palet = forms.ChoiceField(label='Palet: ', choices=(), widget=forms.Select(attrs={'class': 'select-palet'}))
    setor = forms.ChoiceField(label='Setor: ', choices=(), widget=forms.Select(attrs={'class': 'select-setor'}))
    setorLocalizacao = forms.ChoiceField(label='Localizacão: ', choices=(),
                                         widget=forms.Select(attrs={'class': 'select-setor-localizacao'}))
    dataInicoAlocacao = forms.DateField(label="Data Alocação", widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                      attrs={'class': 'form-control',
                                                                                             'type': 'date'}))


class EntradaPalet(ModelForm):
    class Meta:
        model = SuperPalet
        fields = ('codigoBarras', 'quantidadeItens', 'produto', 'tipoEmbalagem', 'paleteria')
        labels = {
            'codigoBarras': ('Código de Barras:'),
            'quantidadeItens': ('Quantidade de Itens:'),
            'produto': ('Produto:'),
            'tipoEmbalagem': ('Embalagem:'),
            'paleteria': ('Paleteria:'),
        }
        # help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código digitado é muito longo"),
                'blank': ('Não é possível armazenar um palet sem um código de barras'),
                'null': ('Não é possível armazenar um palet sem um código de barras')
            },
            'quantidadeItens': {
                'blank': ('Não é possível armazenar um palet sem a quantidade de caixas'),
                'null': ('Não é possível armazenar um palet sem a quantidade de caixas')
            },
            'produto': {
                'blank': ('Não é possível armazenar um palet sem informar o produto'),
                'null': ('Não é possível armazenar um palet sem informar o produto')
            },
            'tipoEmbalagem': {
                'blank': ('Não é possível armazenar um palet sem informar o tipo de embalagem'),
                'null': ('NNão é possível armazenar um palet sem informar o tipo de embalagem')
            },
            'paleteria': {
                'blank': ('Não é possível armazenar um palet sem informar a paleteira'),
                'null': ('Não é possível armazenar um palet sem informar a paleteira')
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
            'codigoBarras': ('Código de Barras:'),
            'quantidadeItens': ('Quantidade de Itens:'),
            'produto': ('Produto:'),
            'tipoEmbalagem': ('Embalagem:'),
            'paleteria': ('Paleteria:'),
            'dataArmazenamento': ('Data de Fabricação')
        }
        # help_texts = {'title': ('Digite o título do projeto'),}
        error_messages = {
            'codigoBarras': {
                'max_length': ("O código digitado é muito longo"),
                'blank': ('Não é possível armazenar um palet sem um código de barras'),
                'null': ('Não é possível armazenar um palet sem um código de barras')
            },
            'quantidadeItens': {
                'blank': ('Não é possível armazenar um palet sem a quantidade de caixas'),
                'null': ('Não é possível armazenar um palet sem a quantidade de caixas')
            },
            'produto': {
                'blank': ('Não é possível armazenar um palet sem informar o produto'),
                'null': ('Não é possível armazenar um palet sem informar o produto')
            },
            'tipoEmbalagem': {
                'blank': ('Não é possível armazenar um palet sem informar o tipo de embalagem'),
                'null': ('NNão é possível armazenar um palet sem informar o tipo de embalagem')
            },
            'paleteria': {
                'blank': ('Não é possível armazenar um palet sem informar a paleteira'),
                'null': ('Não é possível armazenar um palet sem informar a paleteira')
            },
            'dataArmazenamento': {
                'blank': ('Não é possível armazenar um palet sem informar a paleteira'),
                'null': ('Não é possível armazenar um palet sem informar a paleteira')
            }
        }
        widgets = {
            'produto' : forms.Select(attrs={'class': 'form-control select-search'}),
            'dataArmazenamento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'})
        }