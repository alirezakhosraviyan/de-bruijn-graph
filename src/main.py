import networkx as nx
import matplotlib.pyplot as plt
from itertools import product


def create_de_bruijn_graph(k, n):
    g = nx.DiGraph()
    for p in product(tuple(map(str, range(k))), repeat=n):
        code = ''.join(p)
        u = str(code).zfill(n)
        tmp = u[1:]
        for i in range(k):
            v = tmp + str(i)
            g.add_edge(u, v, weight=i)
    return g


def de_bruijn_nx(k, n):
    g = create_de_bruijn_graph(k, n)
    ls = nx.eulerian_circuit(g)
    res = ''.join(map(str, (g.get_edge_data(*e)['weight'] for e in ls)))
    return res


def draw_de_bruijn_graph(g):
    plt.figure(figsize=(20,20), dpi=80)
    nx.draw_networkx(
        g, pos=nx.circular_layout(g),
        node_shape='o', node_size=4000, font_size=20,
        edge_color='#555555', width=3.0
    )
    nx.draw_networkx_edge_labels(
        g, pos=nx.circular_layout(g),
        edge_labels=nx.get_edge_attributes(g, 'weight'),
        font_size=24, label_pos=0.25, rotate=False
    )
    plt.axis('off')
    plt.show()


draw_de_bruijn_graph(create_de_bruijn_graph(2, 3))

