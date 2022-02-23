N = int(input())
a = [int(i) for i in input().split()]
c = [0,0,0]
pos = True
for h in range(len(a)):
    try:
        n = a[h]
        a[h] = c.count(n)
        c[c.index(n)] += 1
    except:
        pos = False
        break
# print(a)
# print(c)
if pos:
    c = 1
    for n in a:
        c *= n%1000000007
    print(c%1000000007)
else:
    print(0)