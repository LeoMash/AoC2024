import copy

f = '6.in'
# f = '6_test.in'

from collections import defaultdict
from functools import cmp_to_key

D = open(f).read().split('\n')
F = []
for line in D:
    F.append([x for x in line])
    pass

print(F)

N = len(F)
M = len(F[0])

def find_start():
    for i in range(N):
        for j in range(M):
            if F[i][j] not in ('.', '#'):
                return i, j
    assert False

DIR4 = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

START_DIR = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3,
}
KEYS = list(START_DIR.keys())

si, sj = find_start()
sd = START_DIR[F[si][sj]]
print(si, sj, sd)

def print_F():
    for i in range(N):
        for j in range(M):
            print(F[i][j], end='')
        print('')

def go1(F):
    x, y, d = si, sj, sd

    while True:
        F[x][y] = KEYS[d]
        dd = DIR4[d]
        nx, ny = x + dd[0], y + dd[1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if F[nx][ny] == '#':
            d = (d + 1) % 4
            continue
        x, y = nx, ny

    ans = 0
    for i in range(N):
        for j in range(M):
            if F[i][j] in KEYS:
                ans += 1
    return ans


def go2(ox, oy):
    x, y, d = si, sj, sd
    vis = set()
    while True:
        if (x, y, d) in vis:
            return True
        vis.add((x, y, d))
        nx, ny = x + DIR4[d][0], y + DIR4[d][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break

        if F[nx][ny] == '#' or nx == ox and ny == oy:
            d = (d + 1) % 4
            continue
        x, y = nx, ny
    return False


F_CP = copy.deepcopy(F)
ans1 = go1(F_CP)
print(ans1)

ans2 = 0
for ox in range(N):
    for oy in range(M):
        ans2 += go2(ox, oy)

print(ans2)
