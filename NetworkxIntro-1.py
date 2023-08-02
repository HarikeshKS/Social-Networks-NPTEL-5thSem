import networkx
import matplotlib.pyplot as plt
g=networkx.Graph()    # this by default creates undirected graph
# g=networkx.DiGraph()    # directed graph
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
print("Nodes in the 1st graph: ",g.nodes())

g.add_edge(1,6)
g.add_edge(3,2)
g.add_edge(2,6)
g.add_edge(2,4)
g.add_edge(4,5)
print("Edges in the 1st graph: ",g.edges())

networkx.draw(g, with_labels=1)    # this draws the graph, the labels are shown by providing the value as true to it.
plt.show()    # this provides the window to show that graph

# For Complete graph:

cg=networkx.complete_graph(10)    # graph of 10 nodes has been created here, where each node is have a connection with each node.
print("Nodes in the Complete graph: ",cg.nodes())
print("Edges in the Complete graph: ",cg.edges())

print(cg.order())    # this shows the number of nodes in the graph
print(cg.size())    # this shows the number of edges in the graph

networkx.draw(cg, with_labels=1)
plt.show()

# Random Graph:
rg=networkx.gnp_random_graph(20,0.5)    # this will create a random graph with 20 nodes and a probability of 0.5 for the edges to be connected.
networkx.draw(rg)
plt.show()