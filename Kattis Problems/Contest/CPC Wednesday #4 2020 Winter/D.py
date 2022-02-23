n = int(input())
p = [int(i) for i in input().split()]
p.sort()
d = 0
for a in range(len(p)-3,-1,-3):
    d += p[a]
# print(p)
print(d)