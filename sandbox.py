import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
plt.plot()
G.add_nodes_from(['x', 'y', 'z', 'f', 'g'])
G.add_edges_from([('x', 'y'), ('x', 'z'), ('x', 'f'), ('g', 'f')])
# nx.draw(G, with_labels=True)
# plt.show()

print(G.nodes)