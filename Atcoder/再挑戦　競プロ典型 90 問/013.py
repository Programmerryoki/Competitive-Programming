from heapq import heappop, heappush
from sys import stdin


def main():
    input = stdin.readline
    N,M = [int(i) for i in input().split()]
    graph = {i:{} for i in range(N)}
    for _ in range(M):
        A,B,C = [int(i) for i in input().split()]
        graph[A-1][B-1] = C
        graph[B-1][A-1] = C

    def djikstra(start):
        dis = [float("inf")]*N
        dis[start] = 0
        que = [(0,start)]
        seen = {start}
        while que:
            d, node = heappop(que)
            if d > dis[node]:
                continue
            for n in graph[node]:
                if n not in seen and d + graph[node][n] < dis[n]:
                    td = d + graph[node][n]
                    dis[n] = td
                    heappush(que, (td, n))
            seen.add(node)
        return dis

    d0 = djikstra(0)
    dl = djikstra(N-1)
    print("\n".join(str(d0[i]+dl[i]) for i in range(N)))


if __name__ == '__main__':
    main()