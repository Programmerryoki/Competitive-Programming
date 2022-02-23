from sys import setrecursionlimit
setrecursionlimit(10**6)
from functools import lru_cache
MOD = 998244353

N = int(input())
S = input()
mul2 = [1]
for i in range(max(N,10)):
    mul2.append(mul2[-1]*2 % MOD)

NS = ""
count = []
j = 0
p = S[0]
S += " "
for i in range(len(S)):
    if S[i] == p:
        continue
    NS += p
    n = i-j
    count.append(mul2[n])
    j = i
    p = S[i]
# print(NS)
# print(count)
LN = len(count)

@lru_cache(None)
def dfs(prev, index, used):
    # print(prev, index, bin(used)[2:])
    if index == LN:
        return 1
    total = 1
    for i in range(index+1, LN):
        if NS[i] == prev:
            total += (dfs(prev, i, used) * (count[i]-1)) % MOD
        else:
            flag = mul2[ord(NS[i]) - ord("A")]
            if used & flag:
                continue
            total += (dfs(NS[i], i, used | flag) * (count[i]-1)) % MOD
    return total % MOD


print(dfs("", -1, 0)-1)