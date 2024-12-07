f = '7.in'
# f = '7_test.in'


def test(res, xs):
    n = len(xs)
    def dfs(cur, idx):
        if idx == n:
            return cur == res
        if dfs(cur + xs[idx], idx + 1):
            return True
        if dfs(cur * xs[idx], idx + 1):
            return True
        return False

    return dfs(0, 0)

def test2(res, xs):
    n = len(xs)
    def dfs(cur, idx):
        if idx == n:
            return cur == res
        if dfs(cur + xs[idx], idx + 1):
            return True
        if dfs(cur * xs[idx], idx + 1):
            return True
        if dfs(int(str(cur) + str(xs[idx])), idx + 1):
            return True
        return False

    return dfs(0, 0)


D = open(f).read().split('\n')
F = []
ans = 0
ans2 = 0
for line in D:
    a, lst = line.split(':')
    a = int(a)
    nums = list(map(int, lst.split()))
    print(a, nums)
    if test(a, nums):
        ans += a
    if test2(a, nums):
        ans2 += a

print(ans)
print(ans2)
