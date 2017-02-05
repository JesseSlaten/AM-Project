import matplotlib.pyplot as plt
import networkx as nx

G=nx.navigable_small_world_graph(2,1,1,2,2) # Not Really sure what to do with this...
nx.draw(G)
plt.show()