class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x,y):
        return self.root(x) == self.root(y)

N = int(input())
edges = [[int(i) for i in input().split()] for j in range(N-1)]
edges.sort(key=lambda x: x[-1])



# from collections import deque
# from sys import stdin
#
# def main():
#     input = stdin.readline
#     N = int(input())
#     graph = {i:{} for i in range(1,N+1)}
#     edges = []
#     for _ in range(N-1):
#         u,v,w = [int(i) for i in input().split()]
#         graph[u][v] = w
#         graph[v][u] = w
#         edges.append((w,u,v))
#     edges.sort(key=lambda x: (-x[0]))
#
#     def bfs(start, other, color, nxtcolor):
#         que = deque([start])
#         seen = {start, other}
#         cs = color[start-1]
#         while que:
#             node = que.popleft()
#             for n in graph[node]:
#                 if n not in seen and cs == color[n-1]:
#                     seen.add(n)
#                     que.append(n)
#                     color[n-1] = nxtcolor
#         color[start-1] = nxtcolor
#         return len(seen)-1
#
#     color = [0]*N
#     colorcount = {0:N}
#     nxtc = 1
#     total = 0
#     for w,u,v in edges:
#         if color[u-1] != color[v-1]:
#             continue
#         oricolor = color[u-1]
#         g = bfs(u,v,color,nxtc)
#         colorcount[oricolor] -= g
#         oc = colorcount[oricolor]
#         colorcount[nxtc] = g
#         nxtc += 1
#         total += g * oc * w
#     print(total)
#
# if __name__ == '__main__':
#     main()