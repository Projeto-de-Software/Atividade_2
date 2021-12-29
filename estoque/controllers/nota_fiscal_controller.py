from datetime import date

from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.core import serializers
from django.http import JsonResponse
import json


def criarNotaFiscal(request):
    if (request.method == 'POST'):
        numero = request.POST.get('numero')
        serie = request.POST.get('serie')
        dataCriacao = request.POST.get('dataCriacao')

        notaFiscal = NotaFiscal(numero=numero, serie=serie, dataCriacao=dataCriacao)
        notaFiscal.save()

        produtos = json.loads(request.POST.get('produtos'))

        for produto in produtos:
            notaFiscalProduto = NotaFiscalProduto(produto_id=produto['produto_id'], notaFiscal_id=notaFiscal.id, quantidade=produto['quantidade'])
            notaFiscalProduto.save()

        return JsonResponse({
            'message': 'Cadastro realizado com sucesso.'
        })

    form = NotaFiscalForm()
    produtos = Produto.objects.all()

    data = {
        'form' : form,
        'produtos': serializers.serialize("json", produtos),
    }

    return render(request, 'views/nota_fiscal/create.html', data)

def listaNotasFiscais(request):
    list = []
    try:
        list = NotaFiscal.objects.all().order_by('status','dataCriacao')
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request, 'views/nota_fiscal/list.html', data)


def checkProdutosSaidaNotaFiscal(request, id):
    if (request.method == 'POST'):
        True
    else:
        produtos = NotaFiscalProduto.objects.filter(notaFiscal_id=id).values()

        for p in produtos:
            palletsAntigos = SuperPalet.objects.filter(produto_id=p['id']).values().order_by('dataArmazenamento')
            quantidadeProduto = p['quantidade']
            palletsIndicados = []

            produtoName = Produto.objects.filter(id=p['produto_id']).first()
            p['produto'] = produtoName

            if (palletsAntigos != None):
                for pallet in palletsAntigos:
                    if quantidadeProduto <= pallet['quantidadeItens']:
                        palletsIndicados.append(pallet)
                        break
                    else:
                        quantidadeProduto = quantidadeProduto - pallet['quantidadeItens']
                        palletsIndicados.append(pallet)

            p['pallets'] = palletsIndicados

        dados = {
            'produtos' : produtos,
            'nota' : NotaFiscal.objects.get(id=id)
        }

        return render(request, 'views/nota_fiscal/check_products.html', dados)

