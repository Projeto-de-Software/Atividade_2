from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse
from ..models import Paleteira

from ..forms import *

class PaleteiraView(ListView):
  model = Paleteira
  context_object_name = 'paleteira_list'
  template_name = 'views/paleteira/list.html'

  def get_queryset(self):
    return Paleteira.objects.filter(rua_id_id=self.kwargs['idRua'] ,sn_ativo=True, sn_deletado=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Paleteira"
    context['idRua'] = self.kwargs['idRua']
    return context

class PaleteiraCreateView(CreateView):
  model = Paleteira
  form_class = PaleteiraForm
  success_url = '/paleteiras/'
  template_name = 'views/paleteira/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Nova Paleteira"
    return context

  def get_initial(self):
    return {'rua_id': Rua.objects.get(id=self.kwargs['idRua'])}

  def get_success_url(self):
    return reverse('paleteiras', kwargs={'idRua': self.kwargs['idRua']})

class PaleteiraUpdateView (UpdateView):
  model = Paleteira
  form_class = PaleteiraForm
  success_url = '/paleteiras/'
  template_name = 'views/paleteira/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    nr_paleteira = Paleteira.objects.get(id=self.kwargs['pk']).nr_paleteira
    context['page_name'] = f'Atualizar paleteira ({nr_paleteira})'
    return context

  def get_initial(self):
    return {'rua_id': Rua.objects.get(id=self.kwargs['idRua'])}

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      paleteira = Paleteira.objects.get(id=kwargs['pk'])
      paleteira.sn_ativo = False

      form = form.save()
      paleteira.save()

      blocos = Bloco.objects.filter(paleteira_id=paleteira)

      for bloco in blocos:
        bloco.paleteira_id_id = form.id
        bloco.save()

      return redirect('paleteiras', idRua=self.kwargs['idRua'])

    return render(request, self.template_name, {'form': form})


class PaleteiraDeleteView (DeleteView):
  model = Paleteira
  success_url = '/paleteiras/'

  def get(self, request, *args, **kwargs):
      paleteira = Paleteira.objects.get(id=kwargs['pk'])
      paleteira.sn_ativo = False
      paleteira.sn_deletado = True
      paleteira.save()
      return redirect('paleteiras', idRua=self.kwargs['idRua'])

  def get_initial(self):
    return {'rua_id': Rua.objects.get(id=self.kwargs['idRua'])}