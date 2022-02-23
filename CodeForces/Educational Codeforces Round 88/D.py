n = int(input())
a = [int(i) for i in input().split()]
i = 0
s = S = 0
for j in range(n):
    while i < n and s + a[i] > 0:
        s += a[i]
        i += 1
    S = max(S, s - max(a[j:i] + [0]))
    if j == i:
        i += 1
    else:
        s -= a[j]
print(S)