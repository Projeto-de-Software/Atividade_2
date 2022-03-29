from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse
from ..models import RuaProduto, Rua
from ..forms import RuaProdutoForm

class RuaProdutoView(ListView):
  model = RuaProduto
  context_object_name = 'produtos'
  template_name = 'views/rua_produto/list.html'

  def get_queryset(self):
    return RuaProduto.objects.filter(rua_id_id=self.kwargs['idRua'] ,sn_ativo=True, sn_deletado=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Paleteira"
    context['idRua'] = self.kwargs['idRua']
    context['form'] = RuaProdutoForm(initial={'rua_id':Rua.objects.get(id=self.kwargs['idRua']) })

    return context

  def post(self, request, *args, **kwargs):
    form = RuaProdutoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('ruasProdutos', idRua=self.kwargs['idRua'])
    return render(request, self.template_name, {'form': form})

class RuaProdutoDeleteView(DeleteView):
  model = RuaProduto
  success_url = '/ruas/'

  def get(self, request, *args, **kwargs):
      rua = RuaProduto.objects.get(id=kwargs['pk'])
      rua.sn_ativo = False
      rua.sn_deletado = True
      rua.save()
      return redirect('ruasProdutos', idRua=self.kwargs['idRua'])


