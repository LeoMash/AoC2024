from collections import defaultdict

# f = '9.in'
f = '9_test.in'

D = open(f).read()
F = [int(x) for x in D]
print(F)

X = []
for i in range(0, len(F), 2):
    v = i // 2
    x = F[i]
    X.extend([v] * x)
    if i + 1 >= len(F):
        break
    x = F[i + 1]
    X.extend(['.'] * x)
print(X)

i = 0
j = len(X) - 1
while i < j:
    while X[i] != '.':
        i += 1
    while X[j] == '.':
        j -= 1
    if i < j:
        X[i], X[j] = X[j], X[i]
        i, j = i + 1, j - 1
print(X)

ans = 0
for i, v in enumerate(X):
    if v == '.':
        break
    ans += i * v
print(ans)