
import matplotlib.pyplot as plt
import networkx as nx
import random as rand
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.pyplot import cm 
from Tkinter import *

#User Interface

root = Tk()
blue = Tk()
#Please set path to image location for this example I placed the image in the wd 
w1 = Label(root,text="Enter a Starting Location:").grid(row=0)
w2 = Label(root,text="Enter a Destination:").grid(row=1)

e1= Entry(root)
e2= Entry(root)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


Button(root,text='Quit',command=root.quit).grid(row=3,column=0, sticky=W,pady=4)

root.mainloop()

#Graphing nodes
e1 = e1.get()
e2 = e2.get()

v= int(e1)
z= int(e2)
G=nx.connected_watts_strogatz_graph(14, 4, .1, 4)
H=nx.Graph() 

# Setting out a start node
H.add_node(1,name='start') 
G.add_node(H)
G.add_edge(H,v)

#Set a minimum length
max_dist = (nx.diameter(G)-1)

#randomize nodes
nodies = nx.nodes(G) 
rand.shuffle(nodies)

#test path length
while nx.shortest_path_length(G,H,nodies[-1]) < max_dist:
    rand.shuffle(nodies)

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
edgecap=[leaving,middle,home]
edgedict={}
for i in range(3):
    edgedict[i]=list(zip(edgecap[i],edgecap[i][1:]))

#Visualization
pos=nx.spring_layout(G)

#Draws color of nodes
cmap=['r','b','g']
nx.draw_networkx_nodes(G,pos,node_color='k')
for x in range(3):
    nx.draw_networkx_nodes(G,pos,nodelist=edgecap[x],color=cmap[x])

#Draws path     
nx.draw_networkx_edges(G,pos)
for x in range(3):
    nx.draw_networkx_edges(G,pos,edgelist=edgedict[x],edge_color=cmap[x],width=10,alpha=.5)

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