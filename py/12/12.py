from collections import defaultdict

f = '12.in'
# f = '12_test.in'

D = open(f).read().split('\n')
F = []
for line in D:
    F.append([x for x in line])
print(F)

N = len(F)
M = len(F[0])

DIR4 = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

RF = []
for i in range(N):
    newline = []
    for j in range(M):
        newline.append(-1)
    RF.append(newline[:])
RSIZE = []
VIS = set()


def bfs(i, j, rnum):
    val = F[i][j]
    sz = 0

    q = [(i, j)]
    while q:
        x, y = q.pop()
        if (x, y) in VIS:
            continue
        if val != F[x][y]:
            continue
        VIS.add((x, y))
        RF[x][y] = rnum
        sz += 1
        for dx, dy in DIR4:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            q.append((nx, ny))
    return rnum, sz


for i in range(N):
    for j in range(M):
        rnum = len(RSIZE)
        rval, rsize = bfs(i, j, rnum)
        if rsize > 0:
            RSIZE.append((rval, rsize))
print(RSIZE)
print(RF)

FENCES = defaultdict(int)
FENCESR = [defaultdict(list) for _ in RSIZE]

for i in range(N):
    for j in range(M):
        val = RF[i][j]
        fm = FENCESR[val]
        for di, (dx, dy) in enumerate(DIR4):
            nx, ny = i + dx, j + dy
            if not (nx < 0 or nx >= N or ny < 0 or ny >= M):
                if RF[nx][ny] == val:
                    continue
            FENCES[val] += 1
            fm[(i, j)].append(di)

print(FENCES)

FENCES2 = [0 for _ in RSIZE]
for r, _ in RSIZE:
    FMRG = list()
    fl = FENCESR[r]
    for (x, y), dlist in fl.items():
        for di in dlist:  # enumerated all fences parts
            to_merge = []
            for fi, ((sx, sy), (ex, ey), fdi) in enumerate(FMRG):  # enumerate existing merged fences - try to merge
                if di == fdi:
                    if di in (0, 2):
                        assert sx == ex
                        if x == sx and sy - 1 <= y <= ey + 1:
                            # found fence to merge - need to update
                            to_merge.append(fi)
                    elif di in (1, 3):
                        assert sy == ey
                        if y == sy and sx - 1 <= x <= ex + 1:
                            # found fence to merge - need to update
                            to_merge.append(fi)
            if to_merge:
                nsx = x
                nsy = y
                nex = x
                ney = y
                for fi in to_merge:
                    (sx, sy), (ex, ey), fdi = FMRG[fi]
                    assert di == fdi
                    if di in (0, 2):
                        assert sx == ex
                        assert sx == x
                    else:
                        assert sy == ey
                        assert sy == y

                    nsx = min(nsx, sx)
                    nsy = min(nsy, sy)
                    nex = max(nex, ex)
                    ney = max(ney, ey)
                    FMRG[fi] = None
                FMRG.append(((nsx, nsy), (nex, ney), di))
                FMRG = [v for v in FMRG if v is not None]
            else:
                # no matching fence found - add new
                FMRG.append(((x, y), (x, y), di))
    FENCES2[r] = len(FMRG)

ans1 = 0
ans2 = 0
for rval, rsize in RSIZE:
    ans1 += rsize * FENCES[rval]
    ans2 += rsize * FENCES2[rval]
print(ans1)
print(ans2)
