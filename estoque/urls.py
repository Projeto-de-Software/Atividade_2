from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),

    path('armazem/criar',armazemCriar , name='criarArmazem'),
    path('armazem', listArmazem, name='listarArmazem'),
    path('armazem/atualizar/<int:id>', atualizarArmazem, name='atualizarArmazem'),
    path('armazem/deletar/<int:id>', deletarArmazem, name='deletarArmazem'),

    path('setor/criar', criarSetor, name='criarSetor'),
    path('setor', listSetor, name='listarSetor'),
    path('setor/atualizar/<int:id>', atualizarSetor, name='atualizarSetor'),
    path('setor/deletar/<int:id>', deletarSetor, name='deletarSetor'),

    path('produto/criar', criarProduto, name='criarProduto'),
    path('produto', listProduto, name='listarProduto'),
    path('produto/atualizar/<int:id>', atualizarProduto, name='atualizarProduto'),
    path('produto/deletar/<int:id>', deletarProduto, name='deletarProduto'),

    path('caixa/criar', criarCaixa, name='criarCaixa'),
    path('caixa/deletar/<int:id>', deletarCaixa, name='deletarCaixa'),
    path('caixa', listCaixa, name='listarCaixa'),
    path('caixa/atualizar/<int:id>', atualizarCaixa, name='atualizarCaixa'),

    path('palet/criar', criarPalet, name='criarPalet'),
    path('palet', listPalet, name='listarPalet'),
    path('palet/atualizar/<int:id>', atualizarPalet, name='atualizarPalet'),
    path('palet/deletar/<int:id>', deletarPalet, name='deletarPalet'),

    path('caixa/saida/<int:id>', caixaSaida, name='saidaCaixa'),

    path('setor/localizacao/<int:id>', setorLocalizacaoList, name='localizacoesSetor'),
    path('setor/localizacao/<int:id>/gerar', criarSetorLocalizacao, name='criarSetorLocalizacao'),

    path('regra', listTipoCaixa, name='listarTipoCaixa'),
    path('regra/criar', criarTipoCaixa, name='criarTipoCaixa'),
    path('regra/atualizar/<int:id>', atualizarTipoCaixa, name='atualizarTipoCaixa'),
    path('regra/deletar/<int:id>', deletarTipoCaixa, name='deletarTipoCaixa'),

    path('movimentacao/entrada', entradaPaletSetor, name='entradaPaletSetor'),
    path('movimentacao', listaMovimentacao, name='listarPaletsArmazenados')

]
