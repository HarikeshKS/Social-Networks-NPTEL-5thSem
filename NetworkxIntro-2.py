import networkx as nx
import matplotlib.pyplot as plt
import random
# Modelling road network of India'a cities

G=nx.Graph()
city_set=["Punjab",
"Rajasthan",
"Sikkim",
"Tamil Nadu",
"Telangana",
"Tripura",
"Uttar Pradesh",
"Uttarakhand",
"West Bengal"]

for i in city_set:
    G.add_node(i)

print(G.nodes())
nx.draw(G, with_labels=1)
# Remember that the draw function will always take artt least one argument.
plt.show()

# Adding cost for the station in the city to get the weights for the same
costs=[]
value=100
while (value<=2000):
    costs.append(value)
    value=value+100
print(costs)

# Adding 16 edges to this network
while (G.number_of_edges()<16):
    c1=random.choice(city_set)    # this will choose a node from the graph G.
    c2=random.choice(city_set)
    if (c1!=c2 and G.has_edge(c1,c2)==0):
        w=random.choice(costs)
        G.add_edge(c1,c2,weight=w)
nx.draw(G,with_labels=1)
plt.show()

# Layouts
'''
There are different types of layouts, that can be used in order to draw the graph of the network.
    1. spring_layout
    2. circular_layout
    3. spectral_layout
these were taught in the lectures ^_^
'''
pos=nx.circular_layout(G)
nx.draw(G)
# for displaying the weights of the edges: 
nx.draw_networkx_edge_labels(G,pos)
plt.show()