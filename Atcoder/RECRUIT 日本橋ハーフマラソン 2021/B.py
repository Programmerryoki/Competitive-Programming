from heapq import heappush, heappop

N = int(input())
E = [[int(i) for i in input().split()] for j in range(N)]
orig = []
for i in range(N):
    for j in range(N):
        heappush(orig, (-E[i][j], i, j))

ans = []
cv = 0
for div in [i for i in range(10,110)]:
    heap = [tuple(i) for i in orig]
    tmp = [[0]*N for i in range(N)]
    ts = 0
    vals = set()
    while heap:
        val, i, j = heappop(heap); val = -val
        rad = int(min(-(-val // (div / 10)), N))
        for (x,y),r in vals:
            if abs(x-i) + abs(y-j) <= max(rad, r):
                break
        else:
            tmp[i][j] = rad
            vals.add(((i,j), rad))
            ts += rad * E[i][j]
    if ts > cv:
        cv = ts
        ans = tmp
for const in [i for i in range(1,N+1)]:
    heap = [tuple(i) for i in orig]
    tmp = [[0]*N for i in range(N)]
    ts = 0
    vals = set()
    while heap:
        val, i, j = heappop(heap); val = -val
        rad = min(const, N)
        for (x,y),r in vals:
            if abs(x-i) + abs(y-j) <= max(rad, r):
                break
        else:
            tmp[i][j] = rad
            vals.add(((i,j), rad))
            ts += rad * E[i][j]
    if ts > cv:
        cv = ts
        ans = tmp
print(cv)
# print("\n".join(" ".join(str(i) for i in j) for j in ans))