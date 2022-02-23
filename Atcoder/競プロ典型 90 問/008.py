from bisect import bisect_left
from functools import lru_cache

MOD = 10**9 + 7

N = int(input())
S = input()
ans = "atcoder"
dp = [[1]*(len(S)+1)]+[[0]*(len(S)+1) for i in range(len(ans))]
for i in range(1,len(ans)+1):
    for j in range(1,len(S)+1):
        dp[i][j] += dp[i][j-1]
        if ans[i-1] == S[j-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= MOD
# for i in dp:
#     print(i)
print(dp[-1][-1])

# words = [[] for i in range(26)]
# for i in range(N):
#     words[ord(S[i]) - ord("a")].append(i)
# print(words)
# @lru_cache(None)
# def recur(cur, index):
#     I = ord(ans[cur])-ord("a")
#     ind = bisect_left(words[I], index)
#     if cur == len(ans)-1:
#         return len(words[I]) - ind
#     tmp = 0
#     for i in words[I][ind:]:
#         tmp += recur(cur+1, i)
#     return tmp % MOD
#
# print(recur(0, 0))