import re

f = '3.in'
D = open(f).read().strip()

R = re.compile("mul\(([0-9]+),([0-9]+)\)")

m = re.findall(R, D)
ans = 0
for a, b in m:
    ans += int(a) * int(b)
print(ans)

ans2 = 0
enabled = True
for i in range(len(D)):
    if enabled and D[i:].startswith("don't()"):
        enabled = False
        continue
    if not enabled and D[i:].startswith("do()"):
        enabled = True
    if not enabled:
        continue
    m = re.match(R, D[i:])
    if m:
        a, b = m.group(1), m.group(2)
        ans2 += int(a) * int(b)
print(ans2)
