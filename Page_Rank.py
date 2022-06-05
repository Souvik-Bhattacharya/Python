# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:36:52 2022

@author: Souvik Bhattacharya
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
G = nx.gnp_random_graph(20,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()
x = random.choice([i for i in range(G.number_of_nodes())])
dict = {}
for i in range(G.number_of_nodes()):
    dict[i] = 0
dict[x] += 1
n = int(input())
for i in range(n):
    L = list(G.neighbors(x))
    if(len(L) == 0):
        x = random.choice([G.number_of_nodes()])
        dict[x] += 1
    else:
        x = random.choice(L)
        dict[x] += 1
sorted_dict = sorted(dict.items(),key = lambda f:f[1])
print(sorted_dict)

pg = nx.pagerank(G)
sorted_pg = sorted(pg.items(),key = lambda f:f[1])
print(sorted_pg)