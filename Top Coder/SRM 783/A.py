T = int(input())
pd = [int(i) for i in input().split()]
nd = [int(i) for i in input().split()]
pdc = {}
for n in pd:
    try:
        pdc[n] += 1
    except:
        pdc[n] = 1
ndc = {}
for n in nd:
    try:
        ndc[n] += 1
    except:
        ndc[n] = 1

stress = 0
for k in ndc.keys():
    try:
        pdc[k] -= ndc[k]
        ndc[k] = 0
    except:
        stress += 1
v = 0
for i in range(1, T+1):
    try:
        pdc[i]
        v += 1
    except:
        continue
print(v, stress)