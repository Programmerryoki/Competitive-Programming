from sys import setrecursionlimit
setrecursionlimit(10**8)

n,m = [int(i) for i in input().split()]
ft = 0
graph = {i:{} for i in range(n)}
for _ in range(m):
    l1,l2,d,c = input().split()
    l1 = int(l1)-1; l2 = int(l2)-1; d = int(d)
    graph[l1].setdefault(l2, [d,c])
    graph[l2].setdefault(l1, [d,c])

mc = float("inf")
def dfs(pos, color, cost):
    global mc
    if len(color) == 7 and pos == 0:
        mc = min(mc, cost)
        return
    if cost >= mc:
        return
    count = 0
    pok = graph[pos]
    for key in pok:
        d,c = pok[key]
        if c in color:
            continue
        count = 1
        dfs(key, color | {c}, cost + d)
    if count == 0:
        for key in pok:
            d,c = pok[key]
            dfs(key, color | {c}, cost + d)

dfs(0, set(), 0)
print(mc)