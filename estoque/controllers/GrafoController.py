import base64
import io
import json

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
import matplotlib.pyplot as plt
import networkx as nx


def loadPageGrafo(request):
    return render(request, 'views/grafo_form.html', {})

def gerarGrafo(request):
    grafo = json.loads(request.POST.get('data'))

    G = nx.Graph()

    # Adicionando os nós
    for no in grafo:
        node = int(no['nome'])
        G.add_node(node)

    # Adicionando as arestas
    for no in grafo:
        for aresta in no["arestas"]:
            node1 = int(no['nome'])
            node2 = int(aresta)
            G.add_edge(node1, node2)

    # Gerando o buffer do grafo
    figure = io.BytesIO()
    nx.draw(G, with_labels=True, font_weight='bold', font_size=8, node_size=1200, node_color='green')
    plt.savefig(figure, format="png")
    figure.seek(0)
    image_png = figure.getvalue()
    figure.close()
    plt.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Gerando o grafo da busca em largura
    if (request.POST.get('tipoBusca') == 'P'):
        figure2 = io.BytesIO()
        T = nx.dfs_tree(G, source=int(request.POST.get('inicio')))
        nx.draw(T, with_labels=True, font_weight='bold', font_size=8, node_size=1200, node_color='red')
        plt.savefig(figure2, format="png")
        figure2.seek(0)
        image_png2 = figure2.getvalue()
        figure2.close()
        plt.close()
        graphic2 = base64.b64encode(image_png2)
        graphic2 = graphic2.decode('utf-8')

        return JsonResponse({'grafo': graphic,
                                                'nomeBusca': 'Busca em Profundidade',
                                                'busca': graphic2})

    # Gerando o grafo da busca em profundidade

    else:
        figure2 = io.BytesIO()
        H = nx.bfs_tree(G, source=int(request.POST.get('inicio')), reverse=False)
        nx.draw(H, with_labels=True, font_weight='bold', font_size=8, node_size=1200, node_color='yellow')
        plt.savefig(figure2, format="png")
        figure2.seek(0)
        image_png2 = figure2.getvalue()
        figure2.close()
        plt.close()
        graphic2 = base64.b64encode(image_png2)
        graphic2 = graphic2.decode('utf-8')

        return JsonResponse({'grafo': graphic,
                                                'nomeBusca': 'Busca em Largura',
                                                'busca': graphic2})









