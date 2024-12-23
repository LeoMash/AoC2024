import sys
from collections import defaultdict, deque
import heapq
import networkx as nx

f = '23.in'
# f = '23_test.in'

D = open(f).read().split('\n')
G = defaultdict(list)
for line in D:
    x, y = line.strip().split('-')
    G[x].append(y)
    G[y].append(x)
G = dict(G)
print(G)

s = set()
for u, nbr in G.items():
    if u.startswith('t'):
        for v in nbr:
            nnbr = G[v]
            for w in nnbr:
                if w in nbr:
                    s.add(tuple(sorted((u, v, w))))

print(s)
ans1 = len(s)
print(ans1)

g = nx.Graph(G)
for u, vlist in G.items():
    g.add_node(u)
    for v in vlist:
        g.add_node(v)
        g.add_edge(u, v)
        g.add_edge(v, u)

print(g)
cliques = nx.algorithms.clique.find_cliques(g)
# print(list(cliques))
max_clique = max(cliques, key = len)
print(max_clique)
ans2 = ','.join(sorted(max_clique))
print(ans2)
