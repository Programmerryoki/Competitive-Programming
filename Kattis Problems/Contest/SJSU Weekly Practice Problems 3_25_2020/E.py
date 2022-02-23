N, p = [int(i) for i in input().split()]
n = [int(i) for i in input().split()]
n.sort()
mi = min(n)
n = [i - mi for i in n]
md = 0
for i,a in enumerate(n):
    if md < p*(i + 1) - a:
        md = p*(i + 1) - a
print(md)