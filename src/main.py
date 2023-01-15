import networkx as nx
from lib.de_bruijn_graph import draw_de_bruijn_graph, create_de_bruijn_graph
from lib.tools import get_fragility, get_robustness, get_random_graphe

# the_graph = create_de_bruijn_graph(2, 5)

# draw_de_bruijn_graph(the_graph)

print('res: ', get_robustness(get_random_graphe([1, 3, 4, 2, 3, 3])))
