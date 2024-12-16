import heapq
from collections import defaultdict

f = '16.in'
# f = '16_test.in'

D = open(f).read().split('\n')
F = []
for line in D:
    F.append([x for x in line])

def printF():
    for f in F:
        print(''.join(f))
    print()

printF()

N = len(F)
M = len(F[0])

for i in range(N):
    for j in range(M):
        if F[i][j] == 'S':
            SX, SY = i, j
            break
print(SX, SY)
SDIR = 0

for i in range(N):
    for j in range(M):
        if F[i][j] == 'E':
            EX, EY = i, j
            break
print(EX, EY)

DIR4 = [
    (0, 1), # east
    (1, 0), # south
    (0, -1), # west
    (-1, 0), # north
]

COST_R = 1000
COST_S = 1

def dijksta(sx, sy, sd):
    dist = [[[10**9 for _ in range(len(DIR4))]  for _ in range(M)] for _ in range(N)]
    dist[sx][sy][0] = 0

    pq = [(0, (sx, sy, sd))]
    while pq:
        cdist, (x, y, d) = heapq.heappop(pq)
        assert F[x][y] != '#'
        if cdist > dist[x][y][d]:
            continue

        # go forward
        dx, dy = DIR4[d]
        nx, ny = x + dx, y + dy
        if F[nx][ny] != '#':
            ndist = cdist + COST_S
            if ndist < dist[nx][ny][d]:
                dist[nx][ny][d] = ndist
                heapq.heappush(pq, (ndist, (nx, ny, d)))
        # rotate right
        nd = (d + 1) % 4
        ndist = cdist + COST_R
        if ndist < dist[x][y][nd]:
            dist[x][y][nd] = ndist
            heapq.heappush(pq, (ndist, (x, y, nd)))

        # rotate left
        nd = (d + 3) % 4
        ndist = cdist + COST_R
        if ndist < dist[x][y][nd]:
            dist[x][y][nd] = ndist
            heapq.heappush(pq, (ndist, (x, y, nd)))

    return min(*dist[EX][EY])

ans1 = dijksta(SX, SY, SDIR)
print(ans1)


def dijksta2(sx, sy, sd):
    dist = [[[10**9 for _ in range(len(DIR4))]  for _ in range(M)] for _ in range(N)]
    dist[sx][sy][0] = 0
    prev = [[[set() for _ in range(len(DIR4))] for _ in range(M)] for _ in range(N)]

    pq = [(0, (sx, sy, sd))]
    while pq:
        cdist, (x, y, d) = heapq.heappop(pq)
        assert F[x][y] != '#'
        if cdist > dist[x][y][d]:
            continue

        # go forward
        dx, dy = DIR4[d]
        nx, ny = x + dx, y + dy
        if F[nx][ny] != '#':
            ndist = cdist + COST_S
            if F[nx][ny] == 'E':
                pass
            if ndist < dist[nx][ny][d]:
                dist[nx][ny][d] = ndist
                heapq.heappush(pq, (ndist, (nx, ny, d)))
                prev[nx][ny][d] = {(x, y, d)}
            elif ndist == dist[nx][ny][d]:
                prev[nx][ny][d].add((x, y, d))
        # rotate right
        nd = (d + 1) % 4
        ndist = cdist + COST_R
        if ndist < dist[x][y][nd]:
            dist[x][y][nd] = ndist
            heapq.heappush(pq, (ndist, (x, y, nd)))
            prev[x][y][nd] = {(x, y, d)}
        elif ndist == dist[x][y][nd]:
            prev[x][y][nd].add((x, y, d))

        # rotate left
        nd = (d + 3) % 4
        ndist = cdist + COST_R
        if ndist < dist[x][y][nd]:
            dist[x][y][nd] = ndist
            heapq.heappush(pq, (ndist, (x, y, nd)))
            prev[x][y][nd] = {(x, y, d)}
        elif ndist == dist[x][y][nd]:
            prev[x][y][nd].add((x, y, d))

    return dist[EX][EY], prev

MIN_DIST_END, PREV = dijksta2(SX, SY, SDIR)

UNIQ_PREV = set()

for ii, dist in enumerate(MIN_DIST_END):
    if dist == ans1:
        def go(x, y, d):
            if (x, y, d) in UNIQ_PREV:
                return
            UNIQ_PREV.add((x, y, d))
            lst = PREV[x][y][d]
            for nx, ny, nd in lst:
                go(nx, ny, nd)

        go(EX, EY, ii)

# print(UNIQ_PREV)
UNIQ_POS = set()
for x, y, _ in UNIQ_PREV:
    UNIQ_POS.add((x, y))

for x, y in UNIQ_POS:
    F[x][y] = 'O'
printF()

ans2 = len(UNIQ_POS)
print(ans2)
