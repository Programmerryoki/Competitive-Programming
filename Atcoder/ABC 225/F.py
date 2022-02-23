from functools import lru_cache

N,K = [int(i) for i in input().split()]
words = [input() for i in range(N)]

small = "z"*N
@lru_cache(None)
def dfs(ind, string, k):
    global small
    if k == K:
        if small > string:
            small = string
        return
    for i in range(ind, len(words)):
        if len(small) <= i:
            dfs(i+1, string+words[i], k+1)
        else:
            tmp = string+words[i]
            for j in range(len(string), min(len(small), len(tmp))):
                if small[j] < tmp[j]:
                    break
            else:
                dfs(i+1, tmp, k+1)


dfs(0, "", 0)
print(small)