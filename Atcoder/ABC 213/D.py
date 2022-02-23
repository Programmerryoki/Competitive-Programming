from heapq import heappush, heappop
from sys import setrecursionlimit
setrecursionlimit(10**6)

N = int(input())
graph = {i:[] for i in range(N)}
for i in range(N-1):
    A,B = [int(i)-1 for i in input().split()]
    heappush(graph[A], B)
    heappush(graph[B], A)

firstContact = {}
order = []
seen = {0}
def dfs(cur):
    global order, seen
    order.append(cur)
    while graph[cur]:
        node = heappop(graph[cur])
        if node in seen:
            continue
        seen.add(node)
        firstContact.setdefault(node, cur)
        dfs(node)
        order.append(cur)
    return

dfs(0)
print(" ".join(str(i+1) for i in order))