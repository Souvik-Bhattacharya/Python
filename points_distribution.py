# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 00:06:09 2022

@author: Souvik Bhattacharya
"""

def add_edges():
    nodes = list(G.nodes())
    for s in nodes:
        for t in nodes:
            if(s!=t):
                r = random.random()
                if(r<=0.5):
                    G.add_edge(s,t)
    return G

def assign_points(G):
    nodes = list(G.nodes())
    L = []
    for c in nodes:
        L.append(100)
    return L

def keep_distributing(points,G):
    while(1):
        new_points = distribute_points(points,G)
        print(new_points)
        points = new_points
        ch = input("0 to stop or any key to continue :")
        if(ch=='0'):
            break
    return new_points

def distribute_points(points,G):
    nodes = list(G.nodes())
    new_point = []
    for i in range(len(nodes)):
        new_point.append(0)
    for i in nodes:
        out = list(G.out_edges(i))
        if(len(out) == 0):
            new_point[i] = new_point[i] + points[i]
        else:
            share = points[i]/len(out)
            for (source,target) in out:
                new_point[target] += share
    return new_point

def rank_by_points(final_points):
    dict = {}
    for i in range(len(final_points)):
        dict[i] = final_points[i]
    print(sorted(dict.items(),key = lambda f:f[1]))

import networkx as nx
import random
import matplotlib.pyplot as plt
n = int(input())
G = nx.DiGraph()
G.add_nodes_from([i for i in range(n)])
G = add_edges()
nx.draw(G,with_labels=True)
plt.show()

points = assign_points(G)
final_points = keep_distributing(points,G)
rank_by_points(final_points)

org_results = nx.pagerank(G)
print(sorted(org_results.items(),key = lambda f:f[1]))