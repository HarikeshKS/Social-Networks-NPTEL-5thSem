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
while (G.number_of_edges()<6):
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
# checking if there is a path between nodes
for i in G.nodes():
    for j in G.nodes():
        print(i, j, nx.has_path(G,j,i))
pos=nx.circular_layout(G)
nx.draw(G, with_labels=1)
# for displaying the weights of the edges: 
nx.draw_networkx_edge_labels(G,pos)
plt.show()

# For calculating the path length between the nodes:

# Checking if the network is connected:
print ("The network G is connected? -> ",nx.is_connected(G))

# to find the shortest path in the network
# Also:
# If there is no edge between any two nodes then, it will throw an exception in the form of error, so we need to handle it.
# import sys -- for using try catch block

try:
    print("Shortest path from Punjab to Tripura: ",nx.dijkstra_path(G,'Punjab','Tripura'))
    print("Length of Shortest path from Punjab to Tripura: ",nx.dijkstra_path_length(G,'Punjab','Tripura'))
except:
    print("No Path between 'Punjab' and 'Tripura'")
nx.draw(G, with_labels=1)
plt.show()

# to find the path that is nearest to the provided source node:
print(nx.single_source_dijkstra_path(G,'Uttar Pradesh'))
nx.draw(G, with_labels=1)
plt.show()


# Meaning of Logarithm: if n means the number then, log of n is the number of digits in n