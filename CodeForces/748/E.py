from collections import deque
from sys import stdin

input = stdin.readline
t = int(input())
for _ in range(t):
    input()
    n,k = [int(i) for i in input().split()]
    graph = {i+1:set() for i in range(n)}
    for _ in range(n-1):
        u,v = [int(i) for i in input().split()]
        graph[u].add(v)
        graph[v].add(u)

    leaf = [1]*(n+1)
    for cur in range(1,n+1):
        if len(graph[cur]) > 1:
            leaf[cur] = 0
    # print(leaf)
    md = [float("inf")]*(n+1)
    for start in range(1,n+1):
        if leaf[start] == 0:
            continue
        md[start] = 1
        que = deque([start])
        seen = {start}
        while que:
            cur = que.popleft()
            for nxt in graph[cur]:
                if nxt not in seen and md[cur] + 1 < md[nxt]:
                    seen.add(nxt)
                    md[nxt] = md[cur] + 1
                    que.append(nxt)
    # print(md)
    count = 0
    for i in range(1,n+1):
        if md[i] > k:
            count += 1
    print(count)