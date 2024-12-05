f = '5.in'
# f = '5_test.in'

from collections import defaultdict
from functools import cmp_to_key

D = open(f).read()
Ds = D.split('\n\n')
assert len(Ds) == 2

R = []
for line in Ds[0].split('\n'):
    R.append([int(x) for x in line.split('|')])

G = defaultdict(set)
for a, b in R:
    G[a].add(b)

def check_line(l):
    for i in range(len(l) - 1):
        if l[i] not in G:
            return False
        for j in range(i + 1, len(l)):
            if l[j] not in G[l[i]]:
                return False
    return True

def my_cmp(a, b):
    if b in G[a]:
        return -1
    if a in G[b]:
        return 1
    return 0

def sort_line(l):
    l2 = l[:]
    l2.sort(key=cmp_to_key(my_cmp))
    return l2

ans = 0
ans2 = 0


for line in Ds[1].split('\n'):
    L = list(map(int, line.split(',')))
    if check_line(L):
        ans += L[len(L) // 2]
    else:
        L2 = sort_line(L)
        ans2 += L2[len(L) // 2]

print(ans)
print(ans2)