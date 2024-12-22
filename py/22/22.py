import sys
from collections import defaultdict, deque
import heapq

f = '22.in'
# f = '22_test.in'

D = open(f).read().split('\n')
F = list(D)
SEEDS = [int(x) for x in F]
print(F)


def get_secrets(seed, ops):
    for i in range(ops):
        seed ^= (seed << 6)
        seed &= 16777215
        seed ^= (seed >> 5)
        seed &= 16777215
        seed ^= (seed << 11)
        seed &= 16777215
        yield seed

print(list(get_secrets(123, 10)))

def solve1(seeds):
    res = 0
    for seed in seeds:
        vals = list(get_secrets(seed, 2000))
        val = vals[-1]
        print(seed, ': ' , val)
        res += val
    return res

# print(solve1(SEEDS))

def get_changes(seed, ops):
    vals = [seed % 10] + [x % 10 for x in get_secrets(seed, ops)]
    l = len(vals)

    keys = set()
    for i in range(4, l):
        val = vals[i]
        assert 0 <= val < 10
        d0 = vals[i - 3] - vals[i - 4]
        d1 = vals[i - 2] - vals[i - 3]
        d2 = vals[i - 1] - vals[i - 2]
        d3 = vals[i] - vals[i - 1]
        key = (d0, d1, d2, d3)
        if key not in keys:
            keys.add(key)
            yield key, vals[i]


def solve2(seeds):
    dd = defaultdict(int)
    for seed in seeds:
        for key, val in get_changes(seed, 2000):
            dd[key] += val
    maxval = 0
    maxkey = None
    for key, val in dd.items():
        if val > maxval:
            maxval = val
            maxkey = key
        print(key, val)
    return maxval, maxkey

# print(list(get_changes(123, 10)))
# print(solve2([1, 2, 3, 2024]))
print(solve2(SEEDS))
