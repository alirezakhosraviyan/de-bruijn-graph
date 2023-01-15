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
    temp_graph = graph.copy()
    list_of_degrees = temp_graph.degree
    sorted_list_of_degrees = sorted(list_of_degrees, key=lambda i: i[1], reverse=True)

    total_sizes = 0
    for cur in sorted_list_of_degrees:
        temp_graph.remove_node(cur[0])
        total_sizes += temp_graph.size()

    return total_sizes / len(sorted_list_of_degrees)
