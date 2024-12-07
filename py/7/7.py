import time

f = '7.in'
# f = '7_test.in'


def test(res, xs):
    n = len(xs)

    def go(cur, idx):
        if cur > res:
            return False
        if idx == n:
            return cur == res
        return go(cur + xs[idx], idx + 1) or \
            go(cur * xs[idx], idx + 1)

    return go(xs[0], 1)


def test2(res, xs):
    n = len(xs)

    def go(cur, idx):
        if cur > res:
            return False
        if idx == n:
            return cur == res
        return go(cur + xs[idx], idx + 1) or \
            go(cur * xs[idx], idx + 1) or \
            go(int(str(cur) + str(xs[idx])), idx + 1)

    return go(xs[0], 1)


def test2_opt(res, xs):
    start = xs[0]
    def go(cur, idx):
        if cur < start:
            return False
        if idx == 0:
            return cur == start

        x = xs[idx]
        if cur % x == 0:
            if go(cur // x, idx - 1):
                return True

        sx = str(x)
        scur = str(cur)
        if scur.endswith(sx):
            ncur = scur[:-len(sx)]
            if ncur and go(int(ncur), idx - 1):
                return True

        return go(cur - x, idx - 1)

    return go(res, len(xs) - 1)



D = open(f).read().split('\n')
F = []
for line in D:
    a, lst = line.split(':')
    a = int(a)
    nums = list(map(int, lst.split()))
    # print(a, nums)
    F.append((a, nums))

ans = 0
for a, nums in F:
    if test(a, nums):
        ans += a
print(ans)

tm = time.time()
ans2 = 0
for a, nums in F:
    if test2(a, nums):
        ans2 += a

print(time.time() - tm)
print(ans2)

tm = time.time()
ans3 = 0
for a, nums in F:
    if test2_opt(a, nums):
        ans3 += a

print(time.time() - tm)
print(ans3)
