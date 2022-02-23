from collections import deque
import copy

N,M = [int(i) for i in input().split()]
graph = {i:set() for i in range(1,N+1)}
for _ in range(M):
    a,b = [int(i) for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)
graphr = copy.deepcopy(graph)
order = []
path = {}
que = deque([1])
seen = set([1])
while que:
    node = que.popleft()
    order.append(node)
    for n in graph[node]:
        if n not in seen:
            path[n] = node
            graphr[n].remove(node)
            que.append(n)
            seen.add(n)

print(graphr)
print(order[::-1])
c = 0
seen = set()
for i in order[::-1]:
    if i not in seen:
        p = []
        que = deque([i])
        seen.add(i)
        while que:
            node = que.popleft()
            p.append(node)
            for n in graphr[node]:
                if n not in seen:
                    seen.add(n)
                    que.append(n)
        print(p)
        c += 1
        del graphr[i]
print(c)