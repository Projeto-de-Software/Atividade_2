from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from ..models import Produto
from ..forms import *

class ProdutoView(ListView):
  model = Produto
  context_object_name = 'produtos_list'
  template_name = 'views/produto/list.html'

  def get_queryset(self):
    return Produto.objects.filter(sn_ativo=True, sn_deletado=False)

class ProdutoCreateView(CreateView):
  model = Produto
  form_class = ProdutoForm
  success_url = '/produtos/'
  template_name = 'views/produto/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Novo Produto"
    return context


class ProdutoUpdateView (UpdateView):
  model = Produto
  form_class = ProdutoForm
  success_url = '/produtos/'
  template_name = 'views/produto/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    nm_produto = Produto.objects.get(id=self.kwargs['pk']).nm_produto
    context['page_name'] = f'Atualizar Produto ({nm_produto})'
    return context

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      produto = Produto.objects.get(id=kwargs['pk'])
      produto.sn_ativo = False

      form.save()
      produto.save()
      return redirect('produtos')

    return render(request, self.template_name, {'form': form})


class ProdutoDeleteView (DeleteView):
  model = Produto
  success_url = '/produtos/'

  def get(self, request, *args, **kwargs):
      produto = Produto.objects.get(id=kwargs['pk'])
      produto.sn_ativo = False
      produto.sn_deletado = True
      produto.save()
      return redirect('produtos')

