from collections import defaultdict

f = '1.in'
D = open(f).read().strip()
d1 = []
d2 = []
d2freq = defaultdict(int)
for line in D.split('\n'):
    a, b = line.split()
    a = int(a)
    b = int(b)
    d1.append(a)
    d2.append(b)
    d2freq[b] += 1
    pass

d1 = sorted(d1)
d2 = sorted(d2)

sum1 = 0
sum2 = 0
for a, b in zip(d1, d2):
    sum1 += abs(a - b)
    sum2 += a * d2freq[a]

print(sum1)
print(sum2)