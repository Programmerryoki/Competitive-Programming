# N, A = [int(i) for i in input().split()]
# x = [int(i) for i in input().split()]
# X = max(x + [A])
# dp = [[[0]*(N*X) for i in range(N)] for j in range(N)]
# dp[0][0][0] = 1
# for j in range(1,N):
#     for k in range(1,N):
#         for s in range(1,N*X):


import collections

n, a = [int(i) for i in input().split()]
x = [int(i) - a for i in input().split()]

sums = collections.Counter([0, x[0]])
for i in x[1:]:
    temp = collections.Counter()
    for s, c in sums.items():
        temp[s + i] += c
    sums += temp

print(sums[0] - 1)
