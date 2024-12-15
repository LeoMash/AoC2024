from collections import defaultdict

f = '15.in'
# f = '15_test.in'

D = open(f).read().split('\n\n')
D1, D2 = D
F = []
for line in D1.split('\n'):
    f = []
    for x in line:
        if x == '@':
            f.append('@')
            f.append('.')
        elif x == 'O':
            f.append('[')
            f.append(']')
        else:
            assert x in ('.', "#")
            f.append(x)
            f.append(x)

    F.append(f)


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


def test_move_v(x, y, dx):
    nx = x + dx
    if F[nx][y] == '#':
        # no move
        return False

    if F[nx][y] == '.':
        return True

    ox = nx
    oy = y
    if F[ox][oy] == ']':
        oy -= 1
    assert F[ox][oy] == '['
    assert F[ox][oy + 1] == ']'
    return test_move_v(ox, oy, dx) and test_move_v(ox, oy + 1, dx)

def move_v(x, y, dx):
    nx = x + dx
    assert F[nx][y] != '#'

    if F[nx][y] == '.':
        F[nx][y] = F[x][y]
        F[x][y] = '.'
        return

    ox = nx
    oy = y
    cp = [F[x][y], '.']
    if F[ox][oy] == ']':
        oy -= 1
        cp = ['.', F[x][y]]
    assert F[ox][oy] == '['
    assert F[ox][oy + 1] == ']'
    move_v(ox, oy, dx)
    move_v(ox, oy + 1, dx)
    F[ox][oy] = cp[0]
    F[ox][oy + 1] = cp[1]
    F[x][y] = '.'


def go_v(x, y, d):
    d = DIR4[d]
    dx, dy = d
    assert dy == 0
    nx = x + dx
    if F[nx][y] == '#':
        # no move
        return x, y

    if F[nx][y] == '.':
        F[nx][y] = F[x][y]
        F[x][y] = '.'
        return nx, y

    ox = nx
    oy = y
    if F[ox][oy] == ']':
        oy -= 1
    assert F[ox][oy] == '['
    assert F[ox][oy + 1] == ']'
    if test_move_v(ox, oy, dx) and test_move_v(ox, oy + 1, dx):
        move_v(ox, oy, dx)
        move_v(ox, oy + 1, dx)

        F[nx][y] = F[x][y]
        F[x][y] = '.'
        return nx, y
    return x, y

def go_h(x, y, d):
    d = DIR4[d]
    dx, dy = d
    assert dx == 0
    ny = y + dy
    oy = ny
    while F[x][oy] in ('[', ']'):
        oy = oy + dy
    if F[x][oy] == '#':
        # no move - blocked
        return x, y
    assert F[x][oy] == '.'
    # move
    for yy in range(oy, y, -dy):
        F[x][yy] = F[x][yy - dy]
    F[x][y] = '.'
    return x, ny

def go(x, y, cmd):
    d = CMD4[cmd]
    if d in (0, 2):
        return go_v(x, y, d)
    else:
        return go_h(x, y, d)


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
        if F[i][j] == '[':
            ans1 += i * 100 + j
print(ans1)
