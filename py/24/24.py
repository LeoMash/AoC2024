import graphlib
import re
import sys
from collections import defaultdict, deque
import heapq
import graphviz
from matplotlib.cbook import flatten

f = '24.in'
# f = '24_test.in'

D = open(f).read()
V = { w: int(v) for w, v in re.findall(r"([a-z0-9]+): ([01])", D) }
G = { w: ( op, a, b ) for a, op, b, w in re.findall(r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", D)}

# print(V)
# print(G)
PART2 = True

X = [w for w in V if w.startswith("x")]
Xval = 0
for x in X:
    idx = int(x[1:])
    val = V[x]
    Xval += (val << idx)
print(Xval)

Y = [w for w in V if w.startswith("y")]
Yval = 0
for y in Y:
    idx = int(y[1:])
    val = V[y]
    Yval += (val << idx)
print(Yval)
Zval = Xval + Yval
print(Zval)


def print_graph():
    dot = graphviz.Digraph(format='png', engine='dot')

    for var in V:
        dot.node(var, var, shape='circle')

    for w, (op, a, b) in G.items():
        gate_name = f'{a}_{b}_{op}'
        dot.node(gate_name, op, shape='box')

        dot.edge(a, gate_name)
        dot.edge(b, gate_name)

        dot.node(w, w, shape='circle')
        dot.edge(gate_name, w)

    output_path = 'circuit_graph_sample'
    dot.render(output_path)

# print_graph()

# retrieved by manually looked in the graph using hints with first bit
swaps = [
    ('z10', 'kmb'),
    ('z15', 'tvp'),
    ('z25', 'dpg'),
    ('vdk', 'mmf')
]

# part2
if PART2:
    for a, b in swaps:
        x, y = G[a], G[b]
        G[b], G[a] = x, y

ORDERED = list(graphlib.TopologicalSorter({ w: { x, y } for w, ( op, x, y ) in G.items() }).static_order())
ORDERED = [w for w in ORDERED if w in G]
print(ORDERED)

for w in ORDERED:
   op, a, b = G[w]
   if   op == "AND": V[ w ] = V[ a ] & V[ b ]
   elif op == "OR":  V[ w ] = V[ a ] | V[ b ]
   elif op == "XOR": V[ w ] = V[ a ] ^ V[ b ]
   else: assert False 

Z = [w for w in V if w.startswith("z")]
ans1 = 0
for z in Z:
    idx = int(z[1:])
    val = V[z]
    ans1 += (val << idx)
print(ans1)

if PART2:
    diff = Zval ^ ans1
    if diff:
        print(diff)
    WRONG_BITS = []
    bitno = 0
    while diff > 0:
        if diff & 1:
            print("LOOK AT z{}".format(bitno))
            break
        diff = diff >> 1
        bitno += 1

print(','.join(sorted(flatten(swaps))))
