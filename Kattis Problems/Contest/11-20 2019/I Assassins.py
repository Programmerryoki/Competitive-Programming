n, m = [int(i) for i in input().split()]
assassins = [1 for i in range(n)]
pa = -1
pt = -1
pp = 0

for a in range(m):
    aa, ak, p = input().split()
    aa = int(aa)
    ak = int(ak)
    p = float(p)
    if pa != ak and pt != aa:
        assassins[ak - 1] -= assassins[aa - 1] * p
    else:
        assassins[ak - 1] -= pp * p

    pa = aa
    pt = ak
    pp = p
    print(assassins)
for a in assassins:
    print(a)


print(0.77 * 0.99)