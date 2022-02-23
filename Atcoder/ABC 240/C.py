from functools import lru_cache

N,X = [int(i) for i in input().split()]
jumps = [[int(i) for i in input().split()] for _ in range(N)]

@lru_cache(None)
def dfs(left, i):
    if i == N:
        return left == 0
    if left < 0:
        return False
    return dfs(left-jumps[i][0], i+1) or dfs(left-jumps[i][1], i+1)

print("Yes" if dfs(X, 0) else "No")