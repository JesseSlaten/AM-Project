import matplotlib.pyplot as plt
import networkx as nx
import random as rand
import numpy as np
import matplotlib.patches as mpatches

# Setting up the graph
v = int(input('Enter number of nodes:'))

G=nx.connected_watts_strogatz_graph(v, 4, .1, 4)
H=nx.Graph() 

# Setting out a start node
H.add_node(1,name='start') 
G.add_node(H)
x=rand.randint(0,v)
G.add_edge(H,x)

#Set a minimum length
max_dist = (nx.diameter(G)-1)

#randomize nodes
nodies = nx.nodes(G) 
rand.shuffle(nodies)

#test path length
while nx.shortest_path_length(G,H,nodies[-1]) < max_dist:
    rand.shuffle(nodies)

#Set destination node. Removes node from list
z = nodies.pop()

#Begining Path
leaving = nx.shortest_path(G,H,z)

#2nd Path       #We could keep 'popping' off random nodes to integrate more paths
while nx.shortest_path_length(G,H,nodies[-1]) < (max_dist/2):
    rand.shuffle(nodies)
j = nodies.pop()
middle = nx.shortest_path(G,z,j)

#Home Bound
home = nx.shortest_path(G,j,H)



#Edge capture
leaving_edges=list(zip(leaving,leaving[1:]))
middle_edges=list(zip(middle,middle[1:]))
home_edges=list(zip(home,home[1:]))


#Visualization
pos=nx.spring_layout(G)

#Draws color of nodes
nx.draw_networkx_nodes(G,pos,node_color='k')
nx.draw_networkx_nodes(G,pos,nodelist=leaving,color='red')
nx.draw_networkx_nodes(G,pos,nodelist=middle,color='blue')
nx.draw_networkx_nodes(G,pos,nodelist=home,color='green')

#Draws path 
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edges(G, pos, edgelist=leaving_edges, edge_color='red',width=10, alpha=.5)
nx.draw_networkx_edges(G,pos,edgelist=middle_edges,edge_color='blue',width=10, alpha=.5)
nx.draw_networkx_edges(G,pos,edgelist=home_edges,edge_color='green',width=10, alpha=.5)

#Label start node
labels={}
labels[H]=r'$Start$'
nx.draw_networkx_labels(G,pos,labels,font_size=16)

#Legends
red= mpatches.Patch(color='red',label='Nodes hit')
black = mpatches.Patch(color='black',label='Node not hit')
blue= mpatches.Patch(color='blue',label='Path Away')
green=mpatches.Patch(color='green',label='Path Home')

plt.legend(handles=[red,black,blue,green],bbox_to_anchor=(1.25,1))
plt.show()

