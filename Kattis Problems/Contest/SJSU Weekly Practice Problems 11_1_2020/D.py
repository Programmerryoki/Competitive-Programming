from collections import defaultdict
import heapq

a = [float(i) for i in input().split()]
b = [float(i) for i in input().split()]
n = int(input())
canon = [[float(i) for i in input().split()]+[j] for j in range(n)]+[a+[n]]+[b+[n+1]]
graph = defaultdict(dict)
for i,[pix,piy,pii] in enumerate(canon):
    for j,[pjx,pjy,pjj] in enumerate(canon):
        if i != j:
            # print(i,j)
            # print(pix,piy,pjx,pjy)
            dis = ((pix - pjx)**2 + (piy - pjy)**2)**0.5
            t = min(2+((50-dis)/5), dis/5)
            if dis >= 50:
                t = min(2+((dis-50)/5), dis/5)
            if pii >= n:
                t = dis/5
            # print("\t",dis,t)
            graph[pii][pjj] = t

# for i in graph:
#     print(i,graph[i])
# print(canon)
mt = [float("inf")]*(n+2)
f = [float("inf")]*(n+2)
que = [[0,n]]
# seen = set()
while que:
    # print(mt)
    # print("\t",que)
    t, p = heapq.heappop(que)
    # print("\t",t,p)
    if t > mt[p]:
        continue
    # print("\t passed")
    if p == n+1:
        print(t)
        exit()
    mt[p] = t
    gp = graph[p]
    for node in gp:
        # if not node in seen:
        if gp[node]+t < mt[node]:
            # print("\t\t",gp[node]+t, node)
            mt[node] = gp[node]+t
            heapq.heappush(que, [gp[node]+t, node])
    # seen.add(p)