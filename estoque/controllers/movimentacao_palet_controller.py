

from django.shortcuts import render, redirect
from ..forms import *
from django.contrib import messages
from django.utils.timezone import now


def entradaPalet (request):
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
    return render(request, 'views/palet/entrada.html', data)

def saidaPaletList(request):
    list = []
    try:
        list = SuperPalet.objects.all().filter(dataRetirada=None).order_by('dataArmazenamento')
    except Exception as e:
        list = []

    data = {
        'list': list
    }
    return render(request, 'views/palet/saida_list.html', data)

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
            objectElemet.dataRetirada = now()
            objectElemet.save()

            messages.success(request, "Palet retirado com sucesso.")

            list = []
            try:
                list = SuperPalet.objects.all().filter(dataRetirada=None).order_by('dataArmazenamento')
            except Exception as e:
                list = []

            data = {
                'list': list
            }
            return render(request, 'views/palet/saida_list.html', data)

        else:
            messages.error(request, "Palet problemas para retirar o palet, tente mais tarde.")
            return render(request, 'views/palet/saida_palet.html', data)
    else:
        return render(request, 'views/palet/saida_palet.html', data)