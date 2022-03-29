from django.urls import path, include
from .controllers import *


urlpatterns = [
    path("produtos/", ProdutoView.as_view() , name='produtos'),
    path("produtos/create", ProdutoCreateView.as_view() , name='produtoCreate'),
    path("produtos/update/<pk>", ProdutoUpdateView.as_view() , name='produtoUpdate'),
    path("produtos/delete/<pk>", ProdutoDeleteView.as_view() , name='produtoDelete'),
    path("ruas/", RuaView.as_view(), name='ruas'),
    path("ruas/create", RuaCreateView.as_view(), name='ruaCreate'),
    path("ruas/update/<pk>", RuaUpdateView.as_view(), name='ruaUpdate'),
    path("ruas/delete/<pk>", RuaDeleteView.as_view(), name='ruaDelete'),
    path("ruas/<idRua>/paleteiras", PaleteiraView.as_view(), name='paleteiras'),
    path("ruas/<idRua>/paleteiras/create", PaleteiraCreateView.as_view(), name='paleteiraCreate'),
    path("ruas/<idRua>/paleteiras/update/<pk>", PaleteiraUpdateView.as_view(), name='paleteiraUpdate'),
    path("ruas/<idRua>/paleteiras/delete/<pk>", PaleteiraDeleteView.as_view(), name='paleteiraDelete'),
    path("ruas/<idRua>/paleteiras/<idPaleteira>/blocos", BlocoView.as_view(), name='blocos'),
    path("ruas/<idRua>/paleteiras/<idPaleteira>/blocos/create", BlocoCreateView.as_view(), name='blocoCreate'),
    path("ruas/<idRua>/paleteiras/<idPaleteira>/blocos/update/<pk>", BlocoUpdateView.as_view(), name='blocoUpdate'),
    path("ruas/<idRua>/paleteiras/<idPaleteira>/blocos/delete/<pk>", BlocoDeleteView.as_view(), name='blocoDelete'),
    path("ruas/<idRua>/produtos", RuaProdutoView.as_view(), name='ruasProdutos'),
    path("ruas/<idRua>/produtos/delete/<pk>", RuaProdutoDeleteView.as_view(), name='ruaProdutoDelete'),

    path("entrada", entradaPalletSelecionarProdutoList, name="entradaProdutoList"),
    path("entrada/<idProduto>", entradaPalletSelecionarLocalizacaoList, name="entradaLocalizacaoList"),
    path("entrada/<idProduto>/<idBloco>/form",entradaPallet , name="entradaFinalizacao"),
    path("movimentacoes", viewMov , name="movimentacoes"),
    path("saida", saidaPalletSelecionarProdutoList, name="saidaProdutoList")

]
