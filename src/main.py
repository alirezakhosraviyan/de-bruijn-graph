import networkx as nx
import matplotlib.pyplot as plt

G = nx.random_regular_graph(5, 6)

subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()