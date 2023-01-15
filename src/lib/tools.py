import networkx as nx
import matplotlib.pyplot as plt


def get_random_graphe(degree_sequence) -> nx.Graph:
    G = nx.random_degree_sequence_graph(degree_sequence, seed=42)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    return G


def get_fragility(graph):
    """returns the special value"""
    adjacency_list = nx.adjacency_spectrum(graph)
    return -max(adjacency_list)


def get_robustness(graph: nx.Graph):
    """returns the robustness value"""
    list_of_degrees = graph.degree
    sorted_list_of_degrees = sorted(list_of_degrees, key=lambda i: i[1], reverse=True)
    graph.remove_node(sorted_list_of_degrees[0][0])

    degrees = next(nx.connected_components(graph))

    return sum(degrees) / len(degrees)
