N,M,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
md = float("inf")
info = None
for i in range(len(A)):
    v = A[i]
    d = float("inf")
    nt = 0
    for j in range(50):
        v *= 1
        v %= K
        if d > K-v:
            d = K - v
            nt = j
    if md > d:
        md = d
        info = (v, i, nt)
    A[i] = [A[i], i]
M -= info[-1]
A[info[1]][0] = info[0]

A.sort(reverse=True)
PW = []

ma = A[0][0]
while M >= 0 and ma*2 < K:
    ma += ma
    M -= 1
    PW.append((A[0][1], A[0][1]))
# print(ma)

vs = {}
for i in range(1,N):
    v = A[i][0]
    while M >= 0 and (v*2) % K < v:
        v += v
        v %= K
        M -= 1
        PW.append((A[i][1], A[0][1]))
    A[i][0] = v
    vs[v] = i

dif = K - ma
md = float("inf")
ind = -1
for v in vs:
    if v == 0:
        continue
    if dif % v == 0 and dif // v <= M:
        PW.append((A[0][1], A[vs[v]][1]))
        break
    else:
        t = dif // v
        d = (ma + v * (t+1)) % K
        if d < md:
            md = d
            ind = v
else:
    PW += [(A[0][1], A[vs[v]][1])]*(dif // v + 1)
print("\n".join(" ".join(str(i) for i in j) for j in PW))