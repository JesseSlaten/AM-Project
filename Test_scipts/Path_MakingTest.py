import matplotlib.pyplot as plt
import networkx as nx
import random as rand
import numpy as np
# Setting up the graph
G=nx.connected_watts_strogatz_graph(10,2,3,4)
H=nx.Graph()
H.add_node(1,name='start') # Setting out a start node
G.add_node(H)
x=rand.randint(0,10)
G.add_edge(H,x)
# Begining path
path = nx.shortest_path(G,H,3)
pos = nx.spring_layout(G)
#Drawing 
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
path_edges= zip(path,path[1:])
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
nx.draw_networkx_nodes(G,pos,nodelist=path,color='g')
labels={}
labels[H]=r'$Start$'
nx.draw_networkx_labels(G,pos,labels,font_size=16)
plt.show()