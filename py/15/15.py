from collections import defaultdict

f = '15.in'
# f = '15_test.in'

D = open(f).read().split('\n\n')
D1, D2 = D
F = []
for line in D1.split('\n'):
    F.append([x for x in line])

CMD = ''.join(D2.split('\n'))

def printF():
    for f in F:
        print(''.join(f))
    print()

printF()
print(CMD)

N = len(F)
M = len(F[0])

for i in range(N):
    for j in range(M):
        if F[i][j] == '@':
            SX, SY = i, j
            break
print(SX, SY)

DIR4 = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

CMD4 = {
    '^': 0,
    '<': 1,
    'v': 2,
    '>': 3,
}

for cmd in CMD:
    assert cmd in CMD4


def go(x, y, cmd):
    d = CMD4[cmd]
    d = DIR4[d]
    dx, dy = d
    nx, ny = x + dx, y + dy
    ox, oy = nx, ny
    while F[ox][oy] == 'O':
        ox, oy = ox + dx, oy + dy
    if F[ox][oy] == '#':
        # no move - blocked
        return x, y
    assert F[ox][oy] == '.'
    # move
    F[x][y] = '.'
    F[ox][oy] = F[nx][ny]
    F[nx][ny] = '@'
    return nx, ny


x, y = SX, SY
for cmd in CMD:
    print('MOVE ', cmd)
    x, y = go(x, y, cmd)
    # printF()
    pass

printF()

ans1 = 0
for i in range(N):
    for j in range(M):
        if F[i][j] == 'O':
            ans1 += i * 100 + j
print(ans1)

ans2 = 0
print(ans2)
