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


#Replace all edges with weighted edges. Can initialize to anything. Using 1 as default
lines= nx.edges(G)
for item in lines:
    u=item[0]
    v=item[1]
    G.remove_edge(u, v)
    G.add_edge(u, v, weight= 1.0)

#Function for modifying weights. 
def getbig (whatevs):
    for item in whatevs:
        u=item[0]
        v=item[1]
        presweight= G[u][v]['weight']
        G[u][v]['weight'] = int(presweight + 10)
    return;

#Set a minimum length
max_dist = (nx.diameter(G)-1)
print(max_dist)

#randomize nodes
nodies = nx.nodes(G)
nodies.remove(H)
rand.shuffle(nodies)

#Begining Path
z = int(input('Enter a Destination:'))
while z == x:
    z = (z+1)%z    
leaving = nx.dijkstra_path(G,H,z, 'weight')
leaving_edges=list(zip(leaving,leaving[1:]))
getbig (leaving_edges)

#2nd Path       
while nx.shortest_path_length(G,z,nodies[-1],weight=None) < (max_dist):
    rand.shuffle(nodies)
j = nodies.pop()
middle = nx.dijkstra_path(G,z,j)
#print ('2nd-route WEIGHT: ', nx.dijkstra_path_length(G,z,j,weight='weight'))
middle_edges=list(zip(middle,middle[1:]))
getbig(middle_edges)

#Home Bound
home = nx.dijkstra_path(G,j,H)
#print ('Home-path WEIGHT: ', nx.dijkstra_path_length(G,j,H,weight='weight'))
home_edges=list(zip(home,home[1:]))
getbig(home_edges) #completely unnecessary 







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



#print to confirm edge weight 
#uplines=nx.get_edge_attributes(G, 'weight')
#print (uplines)  




