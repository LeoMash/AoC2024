import heapq
from collections import defaultdict, deque
from re import search

f = '19.in'
# f = '19_test.in'

D = open(f).read().split('\n\n')
P = [x.strip() for x in D[0].split(',')]
print(P)

O = [x.strip() for x in D[1].splitlines()]
print(O)


cache = {}
def num_split(o):
    if o in cache:
        return cache[o]
    if not o:
        return 1
    num = 0
    for p in P:
        if o.startswith(p):
            num += num_split(o[len(p):])
    cache[o] = num
    return num


ans1 = 0
ans2 = 0
for i, o in enumerate(O):
    n = num_split(o)
    ans1 += n > 0
    ans2 += n
print(ans1)
print(ans2)