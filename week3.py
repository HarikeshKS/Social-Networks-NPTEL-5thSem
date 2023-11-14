import networkx as nx
import itertools

# aim is to divide the graph into two partitions (communities).


def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()
    # get all the combinations of the nodes that may fall in a community

    first_community = []
    for i in range(1, n/2 + 1):
        comb = [list(x) for x in itertools.combinations(nodes, i)]
        first_community.extend(comb)

    second_community = []
    # to perform subtraction on lists, set is used.
    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community[i]))
        second_community.append(l)
    # If a division is good, then the number of intra-community edges should be high, and the number of inter-community edges should be less.
    # Ṇow, which division is the best here?
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    # finding out the ratio for every division that we had made so far.
    ratio = []    # ratio of number of intra/number of inter community edges
    
    for i in range(len(first_community)):
        # G.subgraph(first_community[i])    # takes input as list of edges and returns a graph object, i.e., an induced subgraph
        num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())

    for i in range(len(second_community)):
        num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())

    e = G.number_of_edges()

    for i in range(len(first_community)):
        num_inter_edges.append(e - num_intra_edges1[i] - num_intra_edges2[i])
    
    # Find out the ratio
    for i in range(len(first_community)):
        ratio.append((float)(num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i])
    
    max_value =max(ratio)
    max_index = ratio.index(max_value)

    print('(',first_community[max_index], '),(', second_community[max_index],')')

G = nx.barbell_graph(5,0)
communities_brute(G)