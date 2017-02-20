import matplotlib.pyplot as plt
import networkx as nx
import random as rand
import numpy as np
import matplotlib.patches as mpatches

# Setting up the graph
v = input('Enter number of nodes:')
G=nx.connected_watts_strogatz_graph(v,2,3,4)
H=nx.Graph()

H.add_node(1,name='start') # Setting out a start node
G.add_node(H)
x=rand.randint(0,v)
G.add_edge(H,x)

# Begining path
z = input('Enter a Destination:')
while z == x:
    z = (z+1)%z  
leaving = nx.shortest_path(G,H,z)
j = (z + rand.randint(0,v))%z
middle = nx.shortest_path(G,z,j)
home = nx.shortest_path(G,j,H)

#Visualzation crap
pos=nx.spring_layout(G)
#Clean this up

leaving_edges=zip(leaving,leaving[1:])
middle_edges=zip(middle,middle[1:])
home_edges=zip(home,home[1:])
#Draws color of nodes
nx.draw_networkx_nodes(G,pos,node_color='k')
nx.draw_networkx_nodes(G,pos,nodelist=leaving,color='red')
nx.draw_networkx_nodes(G,pos,nodelist=middle,color='blue')
nx.draw_networkx_nodes(G,pos,nodelist=home,color='green')
#Draws path 
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edges(G,pos,edgelist=leaving_edges,edge_color='red',width=10)
nx.draw_networkx_edges(G,pos,edgelist=middle_edges,edge_color='blue',width=10)
nx.draw_networkx_edges(G,pos,edgelist=home_edges,edge_color='green',width=10)
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
