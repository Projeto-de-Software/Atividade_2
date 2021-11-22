from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home (request):
    return render(request,'base.html')

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
    list = Armazem.objects.all()
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
    list = Caixa.objects.all().order_by('dataFabricacao')
    data = {
        'list': list
    }
    return render(request , 'views/caixa/list.html', data)

def listPalet(request):
    list = Palet.objects.all()
    data = {
        'list': list
    }
    return render(request , 'views/palet/list.html', data)

def listProduto(request):
    list = Produto.objects.all()
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
    return redirect('')

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