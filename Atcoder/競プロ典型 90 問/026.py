from collections import deque

N = int(input())
graph = {i:set() for i in range(N)}
for _ in range(N-1):
    A,B = [int(i)-1 for i in input().split()]
    graph[A].add(B)
    graph[B].add(A)

que = deque([0])
seen = set()
color = [-1]*N
color[0] = 0
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            color[n] = 1 - color[node]
            que.append(n)
            seen.add(n)
check = 0 if color.count(0) > N//2 else 1
# print(color)
print(" ".join([str(i+1) for i in range(N) if color[i] == check][:-(-N//2)]))