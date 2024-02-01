s = 0
p = [1] * 2000000
p[0] = 0
p[1] = 0
for i in range(len(p)):
    if not p[i]:
        continue
    s += i
    for j in range(2*i, len(p), i):
        p[j] = 0
print(s)