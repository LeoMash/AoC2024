from collections import defaultdict

f = '11.in'
# f = '11_test.in'

D = open(f).read().split('\n')[0].split()
F = [int(x) for x in D]
freq = {x : 1 for x in F}

# def blink_sim(xs):
#     q = len(xs)
#     for i in range(q):
#         x = xs[i]
#         if x == 0:
#             xs[i] = 1
#             continue
#         l = len(str(x))
#         if l % 2 == 0:
#             l = l // 2
#             xs[i] = x // (10 ** l)
#             xs.append(x % (10 ** l))
#             continue
#         xs[i] = x * 2024

def blink2(freq):
    nfreq = defaultdict(int)
    for x, cnt in freq.items():
        if x == 0:
            nfreq[1] += cnt
            continue
        l = len(str(x))
        if l % 2 == 0:
            l = l // 2
            nfreq[x // (10 ** l)] += cnt
            nfreq[x % (10 ** l)] += cnt
            continue
        nfreq[x * 2024] += cnt
    return nfreq

ans = [sum(freq.values())]
for i in range(75):
    freq = blink2(freq)
    ans.append(sum(freq.values()))

print(ans[25])
print(ans[75])
