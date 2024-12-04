f = '4.in'
# f = '4_test.in'
D = open(f).read().strip()

num = 0
F = []
FD = []
for line in D.split('\n'):
    F.append([x for x in line])
    FD.append([x for x in line])

N = len(F)
M = len(F[0])

DIR8 = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
]

XMAS = 'XMAS'


def search(i, j):
    nums = 0
    for D in DIR8:
        dir_succ = True
        for k in range(len(XMAS)):
            ni, nj = i + D[0] * k, j + D[1] * k
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                dir_succ = False
                break
            if F[ni][nj] != XMAS[k]:
                dir_succ = False
                break
        if dir_succ:
            nums += 1
    return nums


DIR4 = [
    [-1, -1],
    [+1, -1],
    [+1, +1],
    [-1, +1],
]
MMSS = (
    'MMSS',
    'MSSM',
    'SSMM',
    'SMMS',
)


def search2(i, j):
    if F[i][j] != 'A':
        return 0
    q = ''
    for d in DIR4:
        ni, nj = i + d[0], j + d[1]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            return False
        if F[ni][nj] not in ('M', 'S'):
            return False
        q += F[ni][nj]
    return q in MMSS


num2 = 0
for i in range(N):
    for j in range(M):
        num += search(i, j)
        num2 += search2(i, j)

print(num)
print(num2)
