from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**7)

add = ["dream","dreamer","erase","eraser"]

S = input()
@lru_cache(maxsize=None)
def dfs(ind):
    if ind >= len(S):
        return ind == len(S)
    for w in add:
        if len(w) + ind > len(S):
            continue
        for j in range(len(w)):
            if S[ind+j] != w[j]:
                break
        else:
            if dfs(ind+len(w)):
                return True
    return False

print("YES" if dfs(0) else "NO")