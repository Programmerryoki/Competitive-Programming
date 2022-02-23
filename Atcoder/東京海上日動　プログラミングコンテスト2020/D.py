# N = int(input())
# for _ in range(N):
#     V,W = [int(i) for i in input().split()]
# coding: utf-8

from sys import stdin

def main():
    input = stdin.readline
    m = int(input())
    n = int(input())
    ppl = [[int(i) for i in input().split()] for j in range(n)]
    dp = [float("inf")]*(m+1)
    for i in range(1,n+1):
        new = [float("inf")]*(m+1)
        for j in range(1,m+1):
            if j - ppl[i-1][0] <= 0:
                new[j] = min(dp[j], ppl[i-1][1])
            else:
                new[j] = min(dp[j - ppl[i-1][0]] + ppl[i-1][1], dp[j])
        dp = new
    print(min(dp[m:]))

if __name__ == "__main__":
    main()

# # coding: utf-8
#
# m = int(input())
# n = int(input())
# ppl = [[int(i) for i in input().split()] for j in range(n)]
# dp = [[float("inf")]*(m+1) for i in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if j - ppl[i-1][0] <= 0:
#             dp[i][j] = min(dp[i-1][j], ppl[i-1][1])
#         else:
#             dp[i][j] = min(dp[i-1][j - ppl[i-1][0]] + ppl[i-1][1], dp[i-1][j])
# print(min(dp[-1][m:]))