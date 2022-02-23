from collections import Counter

od = Counter()
ou = Counter()

N,H = [int(i) for i in input().split()]
for _ in range(N//2):
    h = int(input())
    try:
        od[h] += 1
    except:
        od[h] = 1
    h = int(input())
    try:
        ou[h] += 1
    except:
        ou[h] = 1
d = od.most_common()
d.sort()
u = ou.most_common()
u.sort(reverse=True)
print(d,u)
m = float("inf")
nl = 0
i = 0
t = 0
c = 0
for h, n in d:
    t += n
    while i < len(u) and u[i][0] >= H - h:
        c += u[i][1]
        i += 1
    temp = N//2 - t + c
    if m > temp:
        print(N//2-t, c, h, i)
        m = temp
        nl = 1
    elif m == temp:
        nl += 1
print(m, nl)