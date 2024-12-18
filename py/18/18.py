import heapq
from collections import defaultdict, deque
from re import search

f = '18.in'
N = 71
M = 71
NUM = 1024
# f = '18_test.in'
# N = 7
# M = 7
# NUM = 12

D = open(f).readlines()
CMD = []
for line in D:
    CMD.append(list(map(int, line.split(','))))

print(CMD)

F = [['.' for _ in range(N)] for _ in range(M)]
for i in range(NUM):
    x, y = CMD[i]
    F[y][x] = '#'

def printF():
    for f in F:
        print(''.join(f))
    print()

printF()


DIR4 = [
    (0, 1), # east
    (1, 0), # south
    (0, -1), # west
    (-1, 0), # north
]

def bfs(sx, sy, ex, ey):
    vis = set()
    q = deque()
    q.append((sx, sy, 0))

    while q:
        x, y, dist = q.popleft()
        if x == ex and y == ey:
            return dist
        if (x, y) in vis:
            continue
        vis.add((x, y))
        for dx, dy in DIR4:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if F[ny][nx] == '#':
                    continue
                q.append((nx, ny, dist + 1))
    return None

ans1 = bfs(0, 0, N - 1, M - 1)
print(ans1)

for i in range(NUM,len(CMD)):
    print(i)
    x, y = CMD[i]
    F[y][x] = '#'
    test = bfs(0, 0, N - 1, M - 1)
    if test is None:
        print(x, y)
        break