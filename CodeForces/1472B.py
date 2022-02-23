# Greedy
# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     A = [int(i) for i in input().split()]
#     CA = Counter(A)
#     SA = sum(A)
#     if SA & 1: # is the sum odd?
#         print("NO")
#     else:
#         tmp = SA//2
#         tmp = max(tmp&1, tmp - CA[2]*2)
#         if CA[1] >= tmp:
#             print("YES")
#         else:
#             print("NO")


# DP
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    SA = sum(A)
    if SA & 1:
        print("NO")
        continue
    dp = [[0]*(SA+1) for i in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        candy = A[i]
        for j in range(SA):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if dp[i][j] == 0:
                continue
            if dp[i][j+candy] or dp[i][j]:
                dp[i+1][j+candy] = 1
        for j in dp:
            print(j)
        print()
    print("Yes" if dp[-1][SA//2] else "No")