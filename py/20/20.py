import heapq
from collections import defaultdict, deque
from re import search

f = '20.in'
# f = '20_test.in'

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

for i in range(N):
    for j in range(M):
        if F[i][j] == 'E':
            EX, EY = i, j
            break
print(EX, EY)

DIR4 = [
    (0, 1),  # east
    (1, 0),  # south
    (0, -1),  # west
    (-1, 0),  # north
]


def bfs(sx, sy):
    dist = dict()

    q = deque([(0, sx, sy)])
    while q:
        cdist, x, y = q.popleft()
        assert F[x][y] != '#'
        if (x, y) in dist:
            continue

        dist[(x, y)] = cdist
        for dx, dy in DIR4:
            nx, ny = x + dx, y + dy
            if F[nx][ny] != '#':
                q.append((cdist + 1, nx, ny))

    return dist


def calc_reachable(sx, sy, maxjumpdist):
    reachable = set()
    for i in range(-maxjumpdist, maxjumpdist + 1):
        for j in range(-maxjumpdist, maxjumpdist + 1):
            nx, ny = sx + i, sy + j
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            dst = abs(nx - sx) + abs(ny - sy)
            if dst > maxjumpdist:
                continue
            if F[nx][ny] != '#':
                reachable.add((nx, ny, dst))
    return reachable


dist = bfs(SX, SY)
inv_dist = bfs(EX, EY)
basetime = dist[(EX, EY)]
assert inv_dist[(SX, SY)] == basetime


def solve(maxdist, savedist):
    ans = 0
    dd = defaultdict(int)
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if F[i][j] != '#':
                cheat_start_x, cheat_start_y = i, j
                d1 = dist[(cheat_start_x, cheat_start_y)]
                reachable = calc_reachable(i, j, maxdist)
                for cheat_end_x, cheat_end_y, cheat_dist in reachable:
                    assert F[cheat_end_x][cheat_end_y] != '#'
                    d2 = inv_dist[(cheat_end_x, cheat_end_y)]
                    if d1 + d2 + cheat_dist < basetime:
                        diff = basetime - d1 - d2 - cheat_dist
                        dd[diff] += 1
                        if diff >= savedist:
                            ans += 1
    print(sorted([(k, v) for k, v in dd.items() if v > 50]))
    return ans


ans1 = solve(2, 100)
print(ans1)
ans2 = solve(20, 100)
print(ans2)
