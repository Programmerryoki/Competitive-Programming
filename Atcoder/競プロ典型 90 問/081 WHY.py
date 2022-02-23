N,K = [int(i) for i in input().split()]
prof = []
mw = 0
mh = 0
for _ in range(N):
    A,B = [int(i) for i in input().split()]
    prof.append((A,B))
    if A > mh:
        mh = A
    if B > mw:
        mw = B
mw += 1
mh += 1
imos = [[0]*(mw+1) for i in range(mh+1)]
for A,B in prof:
    imos[A+1][B+1] += 1
for i in range(1,mh+1):
    for j in range(1,mw+1):
        imos[i][j] += imos[i-1][j]
for i in range(1,mh+1):
    for j in range(1,mw+1):
        imos[i][j] += imos[i][j-1]
# for i in imos:
#     print(i)
mp = 1
for i in range(mh - K):
    for j in range(mw - K):
        # print(i,j)
        p = imos[i][j] + imos[i+K+1][j+K+1] - imos[i][j+K+1] - imos[i+K+1][j]
        if p > mp:
            mp = p
print(mp)