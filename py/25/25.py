import sys
from collections import defaultdict, deque
import heapq

f = '25.in'
# f = '25_test.in'

D = open(f).read().split('\n\n')
LOCKS = []
KEYS = []
H = 0
W = 0
for pp in D:
    L = []
    for line in pp.split('\n'):
        L.append(line)
        W = len(line)
    H = len(L)
    if pp.startswith('#'):  # lock
        LOCKS.append(L)
    else:
        KEYS.append(L)

# print("LOCKS")
# print(LOCKS)
# print("KEYS")
# print(KEYS)

LOCKS_H = []
for L in LOCKS:
    N = len(L)
    M = len(L[0])
    assert H == N
    assert W == M
    LOCK_H = []
    for i in range(M):
        h = 0
        while h < N and L[h][i] == '#':
            h += 1 
        LOCK_H.append(h - 1)
    LOCKS_H.append(LOCK_H)        

# print(LOCKS_H)

KEYS_H = []
for K in KEYS:
    N = len(K)
    M = len(K[0])
    assert H == N
    assert W == M
    KEY_H = []
    for i in range(M):
        h = 0
        while h < N and K[h][i] == '.':
            h += 1 
        KEY_H.append(N - h - 1)
    KEYS_H.append(KEY_H)
# print(KEYS_H)


ans1 = 0
for L in LOCKS_H:
    for K in KEYS_H:
        for i in range(W):
            if L[i] + K[i] >= H - 1:
                # print(L, K, "FAIL", i, L[i], K[i])
                break
        else:
            # print(L, K, "OK")
            ans1 += 1
print(ans1)