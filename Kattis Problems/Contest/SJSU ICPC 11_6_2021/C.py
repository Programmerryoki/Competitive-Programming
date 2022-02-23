from sys import stdin
from collections import deque

def main():
    input = stdin.readline
    n,m = [int(i) for i in input().split()]
    graph = {i+1:set() for i in range(n)}
    for _ in range(m):
        a,b = [int(i) for i in input().split()]
        graph[a].add(b)
        graph[b].add(a)

    groups = []
    seen = set()
    for i in range(1,n+1):
        if i in seen:
            continue
        que = deque([i])
        gs = 1
        ts = len(graph[i])
        while que:
            cur = que.popleft()
            for nxt in graph[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    que.append(nxt)
                    gs += 1
                    ts += len(graph[nxt])
        groups.append((gs, ts == gs*(gs-1)))
    print(groups)


if __name__ == '__main__':
    main()