from collections import deque

N,M = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if a == b:
    print("Yes")
    exit()
if sum(a) != sum(b):
    print("No")
    exit()
graph = {i:set() for i in range(1,N+1)}
for _ in range(M):
    c,d = map(int, input().split())
    graph[c].add(d)
    graph[d].add(c)


total = set()
order = []
for i in range(1,N+1):
    if i not in total:
        que = deque([i])
        seen = set()
        while que:
            node = que.popleft()
            for n in graph[node]:
                if not n in seen:
                    que.append(n)
                    seen.add(n)
        order.append(seen)
        total.update(seen)
for ord in order:
    if sum([a[i-1] for i in ord]) != sum([b[i-1] for i in ord]):
        print("No")
        break
else:
    print("Yes")