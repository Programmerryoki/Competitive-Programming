from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**9)

def main():
    MOD = 10**9 + 7
    N,M,K = map(int, input().split())

    @lru_cache(None)
    def recur(W, B, UW, UB):
        # print(W,B,UW,UB)
        if W == 0 and B == 0:
            return UW <= UB + K
        total = 0
        if W and UW < UB + K:
                total += recur(W-1, B, UW+1, UB)
        if B:
            total += recur(W, B-1, UW, UB+1)
        return total % MOD
    print(recur(N, M, 0, 0))

if __name__ == '__main__':
    main()

# from sys import setrecursionlimit
# setrecursionlimit(10**9)
#
# MOD = 10**9 + 7
#
# N,M,K = map(int, input().split())
#
# # dp[i][j]
# # i = number of black used
# # j = number of white used
# dp = [[1]+[0]*(N) for i in range(M+1)]
# for i in range(1,M+1):
#     for j in range(1,N+1):
#         if j <= i + K:
#             dp[i][j] += dp[i][j-1]
# for i in dp:
#     print(i)