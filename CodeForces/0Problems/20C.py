from sys import stdin
from heapq import heappush, heappop

def main():
    input = stdin.readline
    n,m = [int(i) for i in input().split()]
    graph = {i+1:{} for i in range(n)}
    for _ in range(m):
        a,b,w = [int(i) for i in input().split()]
        graph[a][b] = w
        graph[b][a] = w
    que = [(0,1)]
    md = [10**20]*(n+1)
    md[1] = 0
    parent = {1:-1}
    while que:
        d, cur = heappop(que)
        if d > md[cur]:
            continue
        for nxt in graph[cur]:
            if d + graph[cur][nxt] < md[nxt]:
                parent[nxt] = cur
                md[nxt] = d + graph[cur][nxt]
                heappush(que, (md[nxt], nxt))
    try:
        end = n
        order = []
        while end != -1:
            order.append(end)
            end = parent[end]
        print(" ".join(map(str, order[::-1])))
    except:
        print(-1)


if __name__ == '__main__':
    main()