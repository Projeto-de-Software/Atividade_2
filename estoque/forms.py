from django.forms import ModelForm
from django import forms
from .models import *

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
        fields = ('codigoBarras', 'dataCriacao', 'quantidadeItens')
        labels = {
            'codigoBarras': ('Código de barras: '),
            'dataCriacao': ('Data de Fabricação: '),
            'quantidadeItens': ('Quantidade de itens suportados: ')
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
            }
        }

        widgets = {
            'dataCriacao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
        }

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'nome' : ('Nome:'),
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
        fields = ('codigoBarras', 'dataFabricacao', 'produto', 'palet')
        labels = {
            'codigoBarras': ('Código de barras: '),
            'dataFabricacao': ('Data de Fabricação: '),
            'produto': ('Produto: '),
            'palet': ('Código do palet: ')
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
            }

        }
        widgets = {
            'dataFabricacao': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control','type': 'date'}),
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



