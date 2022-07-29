import matplotlib.pyplot as plt
import networkx as nx
#  pip install networkx

G = nx.Graph() 
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(4, 7)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(8, 9)
G.add_edge(9, 10)
G.add_edge(10, 1)
G.add_edge(10, 9)

nx.draw(G, with_labels=True, font_weight='bold', font_size = 8, node_size = 1200, node_color='green')
plt.savefig("grafo.png")
plt.close()

T = nx.dfs_tree(G, source=2, depth_limit=8)
nx.draw(T, with_labels=True, font_weight='bold', font_size = 8, node_size = 1200, node_color='red')
plt.savefig("busca_profundidade.png")
plt.close()

H = nx.bfs_tree(G, source=2, reverse=False, depth_limit=8)
nx.draw(H, with_labels=True, font_weight='bold', font_size = 8, node_size = 1200, node_color='yellow')
plt.savefig("busca_largura.png")
plt.close()
