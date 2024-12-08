from collections import defaultdict

f = '8.in'
# f = '8_test2.in'
# f = '8_test.in'

D = open(f).read().split('\n')
F = []
for line in D:
    F.append([x for x in line])
# print(F)

N = len(F)
M = len(F[0])

P = defaultdict(list)
for i in range(N):
    for j in range(M):
        if F[i][j] != '.':
            P[F[i][j]].append((i, j))
# print(P)

ans = set()
ans2 = set()
for k, v in P.items():
    l = len(v)
    for i in range(l - 1):
        for j in range(i + 1, l):
            x1, y1 = v[i]
            x2, y2 = v[j]
            # print(k, (x1, y1), (x2, y2))
            dx, dy = x1 - x2, y1 - y2
            # print(dx, dy)
            # ans1
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 - dx, y2 - dy
            # print('->', (nx1, ny1), (nx2, ny2))
            if 0 <= nx1 < N and 0 <= ny1 < M:
                ans.add((nx1, ny1))
            if 0 <= nx2 < N and 0 <= ny2 < M:
                ans.add((nx2, ny2))
            # ans2
            nx1, ny1 = x1, y1
            while True:
                ans2.add((nx1, ny1))
                nx1, ny1 = nx1 + dx, ny1 + dy
                if (0 > nx1 or nx1 >= N) or (0 > ny1 or ny1 >= M):
                    break
            nx2, ny2 = x2, y2
            while True:
                ans2.add((nx2, ny2))
                nx2, ny2 = nx2 - dx, ny2 - dy
                if (0 > nx2 or nx2 >= N) or (0 > ny2 or ny2 >= M):
                    break

ans = len(ans)
print(ans)

ans2 = len(ans2)
print(ans2)
