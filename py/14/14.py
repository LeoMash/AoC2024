from collections import defaultdict, deque

f = '14.in'
M = 101
N = 103
# f = '14_test.in'
# M = 11
# N = 7

D = open(f).read().split('\n')
R = []
for line in D:
    p, v = line.split()
    p = p.split('=')[1]
    p = [int(x) for x in p.split(',')]
    v = v.split('=')[1]
    v = [int(x) for x in v.split(',')]
    R.append((p, v))

print(R)

TM = 100

ans1 = 0


q = [0] * 4
for p, v in R:
    x, y = p
    vx, vy = v
    x += TM * vx
    x %= M

    y += TM * vy
    y %= N

    # print(x, y, M // 2, N // 2)
    if x == M // 2 or y == N // 2:
        continue
    if x < M // 2:
        if y < N // 2:
            q[0] += 1
        else:
            q[1] += 1
    else:
        if y < N //  2:
            q[2] += 1
        else:
            q[3] += 1

print(q)
ans1 = 1
for qq in q:
    ans1 *= qq
print(ans1)


P = [p for p, _ in R]
V = [v for _, v in R]

def printF(F):
    for f in F:
        print(''.join(f))
    print()

DIR4 = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]



def bfs(sx, sy, vis):
    q = [(sx, sy)]
    while q:
        x, y = q.pop()
        if (x, y) in vis:
            continue
        vis.add((x, y))
        for dx, dy in DIR4:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and F[ny][nx] == '#':
                q.append((nx, ny))


def get_components(F):
    c = 0
    vis = set()
    for x in range(M):
        for y in range(N):
            if F[y][x] == '#' and (x, y) not in vis:
                c += 1
                bfs(x, y, vis)
    return c

t = 0
while True:
    # print(t)
    F = [[' ' for _ in range(M)] for _ in range(N)]
    for (x, y) in P:
        F[y][x] = '#'
    # printF(F)
    # pass
    for i, (p, v) in enumerate(zip(P, V)):
        x, y = p
        vx, vy = v
        x += vx
        x %= M

        y += vy
        y %= N
        P[i] = (x, y)

    cnt = get_components(F)
    if cnt < len(R) // 2:
        # candidate
        printF(F)
        print(t)
        break
    t += 1
