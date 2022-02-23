from sys import stdin
from heapq import heappop, heappush
from collections import deque

def main():
    input = stdin.readline
    MOD = 10**9 + 7

    N,M = [int(i) for i in input().split()]
    graph = {i:set() for i in range(N)}
    for _ in range(M):
        A,B = [int(i)-1 for i in input().split()]
        graph[A].add(B)
        graph[B].add(A)

    def bfs(start):
        parent = [[] for i in range(N)]
        DIS = [float("inf")] * N
        DIS[start] = 0
        que = [(0, start)]
        seen = set()
        while que:
            dis, node = heappop(que)
            if node in seen:
                continue
            for n in graph[node]:
                if DIS[n] > dis + 1:
                    heappush(que, (dis+1, n))
                    DIS[n] = dis + 1
                    parent[n] = [node]
                elif DIS[n] == dis+1:
                    parent[n].append(node)
            seen.add(node)
        return DIS, parent

    distance, parent = bfs(0)
    que = deque([N-1])
    count = [0] * N
    count[-1] = 1
    seen = set()
    while que:
        node = que.popleft()
        if node in seen:
            continue
        for n in parent[node]:
            if n not in seen:
                count[n] += count[node]
                count[n] %= MOD
                que.append(n)
        seen.add(node)
    print(count[0])


if __name__ == '__main__':
    main()