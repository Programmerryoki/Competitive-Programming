from sys import setrecursionlimit
setrecursionlimit(10**8)

N, K = map(int, input().split())
T = [[int(i) for i in input().split()] for j in range(N)]

count = 0
def dfs(cur, seen, cost):
    if len(seen) == N:
        cost += T[cur][0]
        if cost == K:
            global count
            count += 1
        return

    for i in range(N):
        if i in seen:
            continue
        dfs(i, seen | {i}, cost + T[cur][i])

dfs(0,set(),0)
print(count//2)