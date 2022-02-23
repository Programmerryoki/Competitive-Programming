
from heapq import heappop, heappush

N,M = map(int, input().split())
graph = {i:{} for i in range(N)}
for _ in range(M):
    A,B,C,D = [int(i) for i in input().split()]
    graph[A-1][B-1] = (C,D)
    graph[B-1][A-1] = (C,D)

def mintime(C,D,t):
    return round(D**0.5) + C + (D // (round(D**0.5)+1))
    # ori = t + C + (D // (t+1))
    # mt = ori
    # print(C,D,t,mt)
    # mi = int((D**0.45)+C) if D > 100 else 0
    # ma = int(-(-(D**0.5) // 1)+C) if D > 100 else ori - t
    # for dt in range(mi,ma+1):
    #     dif = D // (t + dt + 1)
    #     nt = t+dt + C + (D // (t+dt+1))
    #     # print(mt, nt)
    #     if nt <= mt:
    #         mt = nt
    #     else:
    #         break
    # return mt

mint = [float("inf")]*N
mint[0] = 0
que = [(0,0)]
seen = set()
while que:
    t, node = heappop(que)
    if node in seen:
        continue
    # print(mint, t, node, graph[node])
    gn = graph[node]
    for n in gn:
        if n not in seen:
            C,D = gn[n]
            mt = mintime(C,D,t)
            if mt >= mint[n]:
                continue
            heappush(que, (mt, n))
            mint[n] = mt
    seen.add(node)
print(mint[-1] if mint[-1] != float("inf") else -1)