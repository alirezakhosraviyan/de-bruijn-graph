import networkx as nx
import scipy
import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
from .de_bruijn_graph import create_de_bruijn_graph


def get_random_graphe(degree_sequence) -> nx.Graph:
    G = nx.random_degree_sequence_graph(degree_sequence, seed=42)
    nx.draw(G, with_labels=True, font_weight="bold")
    plt.show()
    return G


def get_adjacency_matrix(graph):
    num_nodes = len(graph.nodes)
    matrix = np.zeros((num_nodes, num_nodes))
    node_index = {node: idx for idx, node in enumerate(graph.nodes)}
    for source, destination in graph.edges:
        source_index = node_index[source]
        destination_index = node_index[destination]
        matrix[source_index, destination_index] = 1
    return matrix


def get_fragility(graph):
    """returns the special value"""
    m = nx.adjacency_matrix(graph)
    eig_values, eig_vectors = scipy.linalg.eig(m.toarray())
    return -max(np.abs(eig_values))


def get_robustness(graph: nx.Graph):
    temp_graph = graph.copy()
    degree_list = temp_graph.degree
    degree_list_sorted = sorted(degree_list, key=lambda i: i[1], reverse=True)
    total_sizes = 0
    robustness = []
    fragilities = []
    for cur in degree_list_sorted:
        temp_graph.remove_node(cur[0])
        Rt = temp_graph.size() / len(degree_list_sorted)
        robustness.append(Rt)
        if temp_graph.edges:
            total_sizes += len(max(nx.weakly_connected_components(temp_graph), key=len))
            fragilities.append(get_fragility(temp_graph))
    return total_sizes / len(degree_list_sorted), robustness, fragilities


def show_linear_model():
    np.polyfit()


def calc_monte(shape):
    graph: nx.Graph = create_de_bruijn_graph(*shape)
    if not graph:
        return 0, 0, 0
    nodes = list(graph.nodes)
    initial_edge_size = graph.size()
    random.shuffle(nodes)
    connected = 0

    while node := nodes.pop():
        graph.remove_node(node)
        if not graph or not nx.is_weakly_connected(graph):
            break
        connected += 1

    p = connected / initial_edge_size
    rob = 0
    fraj = 0
    if graph:
        rob = len(max(nx.weakly_connected_components(graph), key=len)) / initial_edge_size
        fraj = get_fragility(graph)
    return p, fraj, rob


def fit_polynomial_and_draw(inp):
    if inp:
        inp.sort(key=lambda x: x[0])
        pf = PolynomialFeatures(degree=2)
        X = np.array([x[0] for x in inp])
        X = X.reshape(-1, 1)
        y = np.array([x[1] for x in inp])
        X_poly = pf.fit_transform(X)
        lin_reg = LinearRegression()
        lin_reg.fit(X_poly, y)
        plt.figure(figsize=(12, 10))
        plt.scatter(X, y, c="orange")
        plt.plot(X, lin_reg.predict(X_poly), color="black")
        plt.xticks(color="gray")
        plt.yticks(color="gray")
        plt.xlabel("F", color="gray")
        plt.ylabel("R", color="gray")
        plt.show()
