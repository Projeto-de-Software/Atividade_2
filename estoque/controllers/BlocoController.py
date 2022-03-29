from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse
from ..models import Bloco

from ..forms import *

class BlocoView(ListView):
  model = Bloco
  context_object_name = 'bloco_list'
  template_name = 'views/bloco/list.html'

  def get_queryset(self):
    return Bloco.objects.filter(paleteira_id=Paleteira.objects.get(id=self.kwargs['idPaleteira']),sn_ativo=True, sn_deletado=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Blocos"
    context['idRua'] = self.kwargs['idRua']
    context['idPaleteira'] = self.kwargs['idPaleteira']
    return context

class BlocoCreateView(CreateView):
  model = Bloco
  form_class = BlocoForm
  success_url = '/blocos/'
  template_name = 'views/bloco/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_name'] = "Novo Bloco"
    context['idRua'] = self.kwargs['idRua']
    context['idPaleteira'] = self.kwargs['idPaleteira']
    return context

  def get_initial(self):
    return {'paleteira_id': Paleteira.objects.get(id=self.kwargs['idPaleteira'])}

  def get_success_url(self):
    return reverse('blocos', kwargs={'idRua': self.kwargs['idRua'], 'idPaleteira': self.kwargs['idPaleteira']})

class BlocoUpdateView (UpdateView):
  model = Bloco
  form_class = BlocoForm
  success_url = '/blocos/'
  template_name = 'views/bloco/create.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    nm_bloco = Bloco.objects.get(id=self.kwargs['pk']).cd_bloco
    context['page_name'] = f'Atualizar bloco ({nm_bloco})'
    context['idRua'] = self.kwargs['idRua']
    context['idPaleteira'] = self.kwargs['idPaleteira']
    return context

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      bloco = Bloco.objects.get(id=kwargs['pk'])
      bloco.sn_ativo = False

      form.save()
      bloco.save()
      idRua = self.kwargs['idRua']
      idPaleteira = self.kwargs['idPaleteira']
      return redirect('blocos', idRua=idRua, idPaleteira=idPaleteira)

    return render(request, self.template_name, {'form': form})


class BlocoDeleteView (DeleteView):
  model = Bloco
  success_url = '/blocos/'

  def get(self, request, *args, **kwargs):
      bloco = Bloco.objects.get(id=kwargs['pk'])
      bloco.sn_ativo = False
      bloco.sn_deletado = True
      bloco.save()
      return redirect('blocos')

