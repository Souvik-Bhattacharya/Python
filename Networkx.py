import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(2,1),(2,3),(3,4),(4,1),(3,1)])
nx.draw(G,with_labels=True)
plt.show()
G=nx.gnp_random_graph(10,0.5)
print(nx.is_connected(G))
E=nx.gnp_random_graph(25,1)
nx.draw(E)
plt.show()
N=nx.barabasi_albert_graph(25,1)
nx.draw(N)
plt.show()
F = nx.barbell_graph(5,4)
nx.draw(F)
plt.show()
H = nx.complete_graph(5)
nx.draw(H)
plt.show()
I = nx.cycle_graph(5)
nx.draw(I)
plt.show()
J = nx.ladder_graph(6)
nx.draw(J)
plt.show()
K = nx.path_graph(5)
nx.draw(K)
plt.show()
L = nx.star_graph(10)
nx.draw(L)
plt.show()
M = nx.wheel_graph(11)
nx.draw(M)
plt.show()