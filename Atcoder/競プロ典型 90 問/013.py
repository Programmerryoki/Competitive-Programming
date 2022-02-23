from sys import stdin
import heapq

input = stdin.readline
N,M = [int(i) for i in input().split()]
graph = {i:{} for i in range(1,N+1)}
for _ in range(M):
    A,B,C = [int(i) for i in input().split()]
    graph[A][B] = C
    graph[B][A] = C

def recur(start):
    dis = [[float("inf"), i] for i in range(1,N+1)]
    que = [dis[start-1]]
    heap = {start}
    seen = {start}
    dis[start-1][0] = 0
    while que:
        # print(que)
        # print(dis)
        d, node = heapq.heappop(que)
        if node in heap:
            heap.remove(node)
        for n in graph[node]:
            # print(n, seen, heap)
            if n not in seen:
                tmp = d + graph[node][n]
                # print(tmp < dis[n-1][0])
                if tmp < dis[n-1][0]:
                    dis[n-1][0] = tmp
                    if n not in heap:
                        heapq.heappush(que, dis[n-1])
                        heap.add(n)
        seen.add(node)
    return [i[0] for i in dis]

sm1 = recur(1)
# print("\n\n")
smlast = recur(N)
# print(sm1, smlast)
print("\n".join([str(sm1[i] + smlast[i]) for i in range(N)]))