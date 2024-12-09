import heapq
from collections import defaultdict

f = '9.in'
# f = '9_test.in'

D = open(f).read()
F = [int(x) for x in D]
print(F)

X = []
FREE_POS = {}
FILES_POS = {}
FREE_POS_H = []
for i in range(0, len(F), 2):
    v = i // 2
    x = F[i]
    if x > 0:
        FILES_POS[len(X)] = x
        X.extend([v] * x)
    if i + 1 >= len(F):
        break
    x = F[i + 1]
    if x > 0:
        FREE_POS[len(X)] = x
        FREE_POS_H.append(len(X))
        X.extend(['.'] * x)

print(X)
print(FILES_POS)
print(FREE_POS)
print(FREE_POS_H)

i = 0
for j in reversed(FILES_POS):
    file = FILES_POS[j]

    free = 0
    i = 0
    for ii, idx_free in enumerate(FREE_POS_H):
        i = idx_free
        if i >= j:
            break
        assert X[i] == '.'
        free = FREE_POS[i]
        if free >= file:
            break
    else:
        # no free space found
        continue

    if free < file:
        # skip file
        continue

    if i < j:
        # move file
        del FREE_POS[i]
        del FREE_POS_H[ii]
        X[i:i+file] = X[j: j+file]
        X[j: j + file] = ['.'] * file
        i += file
        if free > file:
            FREE_POS[i] = free - file
            FREE_POS_H.append(i)
            FREE_POS_H.sort()
print(X)

ans = 0
for i, v in enumerate(X):
    if v == '.':
        continue
    ans += i * v
print(ans)