from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from ..models import Rua

from ..forms import *

class RuaView(ListView):
  model = Rua
  context_object_name = 'rua_list'
  template_name = 'views/rua/list.html'

  def get_queryset(self):
    return Rua.objects.filter(sn_ativo=True, sn_deletado=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['caminhos'] = [{'name': 'Ruas', 'path': '/ruas'}]
    return context

class RuaCreateView(CreateView):
  model = Rua
  form_class = RuaForm
  success_url = '/ruas/'
  template_name = 'views/rua/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Novo rua"
    return context


class RuaUpdateView (UpdateView):
  model = Rua
  form_class = RuaForm
  success_url = '/ruas/'
  template_name = 'views/rua/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    nm_rua = Rua.objects.get(id=self.kwargs['pk']).nm_rua
    context['page_name'] = f'Atualizar rua ({nm_rua})'
    return context

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      rua = Rua.objects.get(id=kwargs['pk'])
      rua.sn_ativo = False
      form = form.save()
      rua.save()

      paleteiras = Paleteira.objects.filter(rua_id=rua)

      for paleteira in paleteiras:
        paleteira.rua_id_id = form.id
        paleteira.save()

      ruasProdutos = RuaProduto.objects.filter(rua_id=rua)

      for ruasProduto in ruasProdutos:
        ruasProduto.rua_id_id = form.id
        ruasProduto.save()

      return redirect('ruas')

    return render(request, self.template_name, {'form': form})

class RuaDeleteView (DeleteView):
  model = Rua
  success_url = '/ruas/'

  def get(self, request, *args, **kwargs):
      rua = Rua.objects.get(id=kwargs['pk'])
      rua.sn_ativo = False
      rua.sn_deletado = True
      rua.save()
      return redirect('ruas')

