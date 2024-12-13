from collections import defaultdict

f = '13.in'
# f = '13_test.in'

D = open(f).read().split('\n')
D.append('')


def solve1(a, b, c):
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c

    D1 = (c1 * b2 - c2 * b1)
    D2 = (c1 * a2 - c2 * a1)
    D = (a1 * b2 - a2 * b1)
    if D != 0 and D1 % D == 0 and D2 % D == 0:
        x = D1 / D
        y = -D2 / D
        if x >= 0 and y >= 0:
            return int(x), int(y)
    return None, None


SHIFT = 10000000000000

ans1 = 0
ans2 = 0
for idx in range(0, len(D), 4):
    a = D[idx].split(':')[1].split(',')
    a = [int(x.split('+')[1]) for x in a]
    b = D[idx + 1].split(':')[1].split(',')
    b = [int(x.split('+')[1]) for x in b]
    c = D[idx + 2].split(':')[1].split(',')
    c = [int(x.split('=')[1]) for x in c]

    print(a, b, c)

    x, y = solve1(a, b, c)
    print(x, y)
    if x is not None:
        print(x * 3 + y)
        ans1 += x * 3 + y
    c[0] += SHIFT
    c[1] += SHIFT
    x, y = solve1(a, b, c)
    print(x, y)
    if x is not None:
        print(x * 3 + y)
        ans2 += x * 3 + y

print(ans1)
print(ans2)
