from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.core import serializers
from django.contrib import messages
import datetime

# Create your views here.
def home (request):
    form = EntradaPalet(request.POST or None)

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            messages.success(request, "Cadastro realizado com sucesso.")
        else:
            messages.error(request, "Não foi possível realizar o cadastro")
    form = EntradaPalet()
    data = {
        'form': form,
    }
    return render(request, 'home.html', data)

def saidaPaletList(request):
    list = []
    try:
        list = SuperPalet.objects.all().filter(dataRetirada=None).order_by('dataArmazenamento')
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request, 'views/saida_list.html', data)

def saidaPalet(request, id):
    data ={}
    objectElemet = SuperPalet.objects.get(id=id)
    form = SaidaPalet(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.codigoBarras,
        'id': objectElemet.id,
        'form':form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            request.method = "GET"
            messages.success(request, "Palet retirado com sucesso.")

            list = []
            try:
                list = SuperPalet.objects.all().filter(dataRetirada=None).order_by('dataArmazenamento')
            except Exception as e:
                list = []

            data = {
                'list': list
            }
            return render(request, 'views/saida_list.html', data)

        else:
            messages.error(request, "Palet problemas para retirar o palet, tente mais tarde.")
            return render(request, 'views/saida_palet.html', data)
    else:
        return render(request, 'views/saida_palet.html', data)


def armazemCriar(request):
    form = ArmazenForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('listarArmazem')
    else:
        form = ArmazenForm()
        data = {'form': form}
        return render(request, 'views/armazen/create.html', data)

def criarSetor(request):
    form = SetorForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('listarSetor')
    else:
        form = SetorForm()
        data = {'form': form}
        return render(request, 'views/setor/create.html', data)

def criarCaixa(request):
    form = CaixaForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('listarCaixa')
    else:
        form = CaixaForm()
        data = {'form': form}
        return render(request, 'views/caixa/create.html', data)

def criarPalet(request):
    form = PaletForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('listarPalet')
    else:
        form = PaletForm()
        data = {'form': form}
        return render(request, 'views/palet/create.html', data)

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

def listArmazem(request):
    list = []
    try:
        list = Armazem.objects.all()
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request , 'views/armazen/list.html', data)

def listSetor(request):
    list = Setor.objects.all()
    data = {
        'list': list
    }
    return render(request , 'views/setor/list.html', data)

def listCaixa(request):
    list = []
    try:
        list = Caixa.objects.all().order_by('dataFabricacao')
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request , 'views/caixa/list.html', data)

def listPalet(request):
    list = []
    try:
        list = Palet.objects.all()
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request , 'views/palet/list.html', data)

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

def atualizarArmazem(request, id):
    data ={}
    objectElemet = Armazem.objects.get(id=id)
    form = ArmazenForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.nomeArmazem,
        'id': objectElemet.id,
        'form':form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarArmazem')
    else:
        return render(request, 'views/armazen/update.html', data)

def atualizarSetor(request, id):
    data ={}
    objectElemet = Setor.objects.get(id=id)
    form = SetorForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.nomeSetor,
        'id': objectElemet.id,
        'form': form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarSetor')
    else:
        return render(request, 'views/setor/update.html', data)

def atualizarCaixa(request, id):
    data ={}
    objectElemet = Caixa.objects.get(id=id)
    form = CaixaForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.codigoBarras,
        'id': objectElemet.id,
        'form': form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarCaixa')
    else:
        return render(request, 'views/caixa/update.html', data)

def atualizarPalet(request, id):
    data ={}
    objectElemet = Palet.objects.get(id=id)
    form = PaletForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.codigoBarras,
        'id': objectElemet.id,
        'form': form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarPalet')
    else:
        return render(request, 'views/palet/update.html', data)

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

def deletarArmazem(request, id):
    objectElemet = Armazem.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarArmazem')

def deletarSetor(request, id):
    objectElemet = Setor.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarSetor')

def deletarCaixa(request, id):
    objectElemet = Caixa.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarCaixa')

def deletarPalet(request, id):
    objectElemet = Palet.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarPalet')

def deletarProduto(request, id):
    objectElemet = Produto.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarProduto')


def caixaSaida(request, id):
    data = {}
    objectElemet = Caixa.objects.get(id=id)
    form = CaixaSaidaForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.codigoBarras,
        'id': objectElemet.id,
        'form': form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarCaixa')
    else:
        return render(request, 'views/movimentacao/caixa_saida.html', data)


def setorLocalizacaoList(request, id):
    list = []
    try:
        list = SetorLocalizacao.objects.filter(setor_id=id)
    except Exception as e:
        list = []

    setor = Setor.objects.get(id=id)
    data = {
        'list': list,
        'setor': setor
    }

    return render(request, 'views/setor/localizacao.html', data)


def criarSetorLocalizacao(request, id):
    data = {}
    setorLocalizacoes = None
    form = None

    setor = id

    form = SetorLocalizacaoForm(request.POST or None)
    setor = Setor.objects.get(id=id)

    if(request.method == 'POST'):
        quantidadeColuna = int(form.data['coluna'])+1
        quantidadeLinha = int(form.data['linha'])+1
        for i in range(1,quantidadeColuna,1):
            for j in range (1,quantidadeLinha,1):
                try:
                    isCreate = SetorLocalizacao.objects.get(coluna=i,linha=j,setor_id=id)
                except Exception as e:
                    setorLocalizacao = SetorLocalizacao(coluna=i, linha=j, setor_id=id)
                    setorLocalizacao.save()

        return redirect(reverse('localizacoesSetor', kwargs={"id": id}))
    else:
        form = SetorLocalizacaoForm()
        form.fields['setor'].initial = setor.id
        data = {
            'form': form,
            'nome': setor.nomeSetor,
            'id': setor.id
        }
        return render(request, 'views/setor/generation_localization.html', data)


def criarTipoCaixa(request):
    form = TipoCaixaForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('listarTipoCaixa')
    else:
        form = TipoCaixaForm()
        data = {'form': form }
        return render(request, 'views/tipo_caixa/create.html', data)

def deletarTipoCaixa(request, id):
    objectElemet = TipoCaixa.objects.get(id=id)
    if (objectElemet != None):
        objectElemet.delete()
    return redirect('listarTipoCaixa')

def atualizarTipoCaixa(request, id):
    data ={}
    objectElemet = TipoCaixa.objects.get(id=id)
    form = TipoCaixaForm(request.POST or None, instance=objectElemet)
    data = {
        'nome': objectElemet.__str__(),
        'id': objectElemet.id,
        'form': form
    }

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            return redirect('listarTipoCaixa')
    else:
        return render(request, 'views/tipo_caixa/update.html', data)


def listTipoCaixa(request):
    list = TipoCaixa.objects.all()
    first = None
    try:
        first = list.first()
    except Exception as e:
        first = None

    data = {
        'list': ([] if first == None else list)
    }

    return render(request , 'views/tipo_caixa/list.html', data)


def listPaletSetor():
    return True

def entradaPaletSetor(request):

    if(request.method == 'POST'):
        form = EntradaPaletSetorForm(request.POST or None)

        paletSetor = PaletSetor()
        paletSetor.setorLocalizacao_id = request.POST['setorLocalizacao']
        paletSetor.dataInicoAlocacao = request.POST['dataInicoAlocacao']
        paletSetor.palet_id = request.POST['palet']
        paletSetor.save()

        return redirect('listarPaletsArmazenados')

    else:
        paletes = Palet.objects.exclude(paletsetor__in=PaletSetor.objects.all())
        setores = Setor.objects.all()
        paletsLocais = PaletSetor.objects.filter(dataFimAlocacao = None)
        setorLocalizacaoDisponivel = SetorLocalizacao.objects.exclude(paletsetor__in = paletsLocais)
        form = EntradaPaletSetorForm()

        data =  {
            'palets': serializers.serialize("json",paletes),
            'setores' : serializers.serialize("json",setores),
            'setoresLocalizacao': serializers.serialize("json",setorLocalizacaoDisponivel),
            'form': form
        }

        return render(request, 'views/movimentacao/palet_setor.html', data)

def listaMovimentacao(request):
    list = PaletSetor.objects.all().filter(dataFimAlocacao = None)
    first = None
    try:
        first = list.first()
    except Exception as e:
        first = None

    data = {
        'list': ([] if first == None else list)
    }

    return render(request, 'views/movimentacao/list.html', data)

def saidaPaletSetor(request):
    return