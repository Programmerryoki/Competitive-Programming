N = int(input())
A = [int(i) for i in input().split()]
count = {}
for a in A:
    count.setdefault(a, 0)
    count[a] += 1
m = 0
for k in count:
    c = count[k]
    if k-1 in count:
        c += count[k-1]
    if k+1 in count:
        c += count[k+1]
    m = max(m, c)
print(m)