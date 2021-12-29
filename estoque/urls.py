from django.urls import path, include
from .controllers import *

urlpatterns = [
    path('', entradaPalet, name='home'),

    path('produto/criar', criarProduto, name='criarProduto'),
    path('produto', listProduto, name='listarProduto'),
    path('produto/atualizar/<int:id>', atualizarProduto, name='atualizarProduto'),
    path('produto/deletar/<int:id>', deletarProduto, name='deletarProduto'),

    path('saida', saidaPaletList, name='saidaPaletList'),
    path('saida/<int:id>', saidaPalet, name='saidaPalet'),


    path('nota/criar', criarNotaFiscal ,name='criarNotaFisca'),
    path('nota/', listaNotasFiscais ,name='listarNotaFisca'),
    path('nota/check/<int:id>', checkProdutosSaidaNotaFiscal ,name='checkProdutosNotaFiscal')

]
