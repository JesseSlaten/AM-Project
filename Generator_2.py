import matplotlib.pyplot as plt
import networkx as nx
import random 
import numpy as np

G=nx.connected_watts_strogatz_graph(10,2,3,4)
H=nx.Graph()
H.add_node(1,name='start')
G.add_node(H)
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos=pos)
nx.draw_networkx_edges(G,pos)
plt.show()
