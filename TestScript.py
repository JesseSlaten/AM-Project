import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
H=nx.path_graph(100)
G.add_nodes_from(H)
nx.draw_random(G)
plt.show()
plt.savefig("Random_Generator")