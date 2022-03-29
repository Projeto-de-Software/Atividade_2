import math
from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from ..models import *
from ..forms import *
from django.db.models import Q
from django.core import serializers
import datetime

# Selecionar/List produto que vai dar entrada no estoque
def entradaPalletSelecionarProdutoList(request):
    produtos = Produto.objects.filter(sn_ativo=True, sn_deletado=False)
    data = {
        'produtos_list' : produtos
    }
    return render(request, 'views/palet/entrada/entradaProdutoList.html', data)

# Seleciona/List onde este produto vai ser armazenado
def entradaPalletSelecionarLocalizacaoList(request, idProduto):
    # Pegando o produto selecionado

    produto = Produto.objects.get(id=idProduto)

    # Pegando as ruas relacionadas com o produto onde este produto pode ser armazenado
    ruasProdutosIndicados = RuaProduto.objects.filter(sn_ativo=True, sn_deletado=False, produto_id=produto)

    blocosOcupadosPallet = PalletBloco.objects.filter(dt_saida__isnull=True)
    blocosOcupados = Bloco.objects.filter(palletbloco__in=blocosOcupadosPallet)

    blocosOcupadosIds = blocosOcupados.values('id')
    blocosLivres = Bloco.objects.filter(sn_deletado=False, #Bloco não deletado
                                          sn_ativo=True, #Bloco Ativo
                                          paleteira_id__sn_ativo=True, #Paleteira ativa
                                          paleteira_id__sn_deletado=False, #Paleteira não deletada
                                          paleteira_id__rua_id__sn_ativo=True, #Rua ativa
                                          paleteira_id__rua_id__sn_deletado=False, #Rua não deletada
                                          palletbloco__dt_saida__isnull=True, #Blocos ocupados
                                          paleteira_id__rua_id__ruaproduto__in=ruasProdutosIndicados,
                                    ).exclude(id__in=blocosOcupadosIds)

    data = {
        'blocos_list': blocosLivres,
        'produto': produto
    }
    return render(request, 'views/palet/entrada/entradaLocalizacaoList.html', data)


# Realiza a entrada do pallet
def entradaPallet(request, idProduto, idBloco):
    form = EntradaPalletForm(initial={'produto_id': Produto.objects.get(id=idProduto)})
    if (request.method == 'GET'):
        data = {
            'form': form
        }
        return render(request, 'views/palet/entrada/entradaPallet.html', data)
    else:
        form = EntradaPalletForm(request.POST)
        if(form.is_valid()):
            pallet = Pallet.objects.get(id=form.save().id)

            qt_unidade_caixas = None

            if(pallet.tp_embalagem == "PA"):
                qt_unidade_caixas = Produto.objects.get(id=idProduto).qt_unid_cx_papelao
            else:
                qt_unidade_caixas = Produto.objects.get(id=idProduto).qt_unid_cx_papelao

            qt_caixas = math.ceil((pallet.qt_unidade/qt_unidade_caixas))
            qt_aux = pallet.qt_unidade
            for i in range (1, qt_caixas+1, 1):
                if (qt_aux > qt_unidade_caixas):
                    Caixa(pallet_id=pallet, qt_unidade=qt_unidade_caixas).save()
                    qt_aux = qt_aux - qt_unidade_caixas
                else:
                    Caixa(pallet_id=pallet, qt_unidade=qt_aux).save()

            PalletBloco(pallet_id=pallet, bloco_id_id=idBloco).save()
            MovPallet(pallet_id=pallet, qt_unidade=pallet.qt_unidade, tp_movimentacao='E').save()

        return viewMov(request)

def viewMov(request):
    data = {
        "movimentacoes": MovPallet.objects.all().order_by('-id'),
        "page_name": "Histórico de movimentações"
    }
    return render(request, 'views/palet/movimentacoes.html', data)

# Seleciona/List o produto que vai sair do estoque
def saidaPalletSelecionarProdutoList(request):
    produtos = Produto.objects.filter(sn_ativo=True, sn_deletado=False)
    data = {
        'produtos_list': produtos
    }
    return render(request, 'views/palet/saida/saidaProdutoList.html', data)

# Seleciona/List o pallet de que vai sair os produtos
def saidaPalletSelecionarItemList(request):
    return
# Realiza a saida do pallet
def saidaPallet(request):
    return
