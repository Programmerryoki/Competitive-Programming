N,P = [int(i) for i in input().split()]
prof = [int(i)-P for i in input().split()]
# print(prof)
mp = 0
s = 0
for i in range(len(prof)):
    s = max(0, s+prof[i])
    mp = max(mp, s)
print(mp)