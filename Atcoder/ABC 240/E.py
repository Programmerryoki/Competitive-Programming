from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
input = stdin.readline

N = int(input())
graph = [set() for i in range(N)]
for _ in range(N-1):
    u,v = [int(i)-1 for i in input().split()]
    graph[u].add(v)
    graph[v].add(u)

group = [[float("inf"),-float("inf")] for _ in range(N)]
b = 1
def dfs(cur, prev):
    global b, group
    if group[cur][0] > b:
        group[cur][0] = b
    if group[cur][1] < b:
        group[cur][1] = b

    if len(graph[cur]) == 1 and cur != 0:
        return
    leaf = True
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)
        b += 1
        leaf = False
    if not leaf:
        b -= 1

    if group[cur][0] > b:
        group[cur][0] = b
    if group[cur][1] < b:
        group[cur][1] = b

dfs(0, -1)
print("\n".join(" ".join(str(i) for i in j) for j in group))