from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from ..models import *
from ..forms import *
from django.core import serializers
from django.contrib import messages
from django.utils.timezone import now

def criarProduto(request):
    form = ProdutoForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('listarProduto')
    else:
        form = ProdutoForm()
        data = {'form': form}
        return render(request, 'views/produto/create.html', data)


def atualizarProduto(request, id):
    data ={}
    objectElemet = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.nome,
        'id': objectElemet.id,
        'form': form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarProduto')
    else:
        return render(request, 'views/produto/update.html', data)

def deletarProduto(request, id):
    objectElemet = Produto.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarProduto')

def listProduto(request):
    list = []
    try:
        list = Produto.objects.all()
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request , 'views/produto/list.html', data)