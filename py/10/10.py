from collections import defaultdict

f = '10.in'
# f = '10_test.in'

D = open(f).read().split('\n')
F = []
for line in D:
    F.append([int(x) for x in line])
print(F)

N = len(F)
M = len(F[0])

start = []
end = []
for i in range(N):
    for j in range(M):
        if F[i][j] == 0:
            start.append((i, j))

DIR4 = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

def dfs(sx, sy, vis):
    cur = F[sx][sy]
    if cur == 9:
        p1 = (sx, sy) not in vis
        vis.add((sx, sy))
        return p1, 1

    p1, p2 = 0, 0
    for dx, dy in DIR4:
        nx, ny = sx + dx, sy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        nval = F[nx][ny]
        if nval != cur + 1:
            continue
        dp1, dp2 = dfs(nx, ny, vis)
        p1 += dp1
        p2 += dp2
    return p1, p2

ans1 = 0
ans2 = 0
for sx, sy in start:
    vis = set()
    p1, p2 = dfs(sx, sy, vis)
    ans1 += p1
    ans2 += p2

print(ans1)
print(ans2)
