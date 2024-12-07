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


D = open(f).read().split('\n')
F = []
for line in D:
    a, lst = line.split(':')
    a = int(a)
    nums = list(map(int, lst.split()))
    # print(a, nums)
    F.append((a, nums))

tm = time.time()
ans = 0
ans2 = 0
for a, nums in F:
    if test(a, nums):
        ans += a
    if test2(a, nums):
        ans2 += a

print(time.time() - tm)
print(ans)
print(ans2)
