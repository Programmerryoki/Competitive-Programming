from bisect import bisect_left
from collections import defaultdict

n,g,t = map(int, input().split())
c = [int(i) for i in input().split()]
c.sort()
dp = [[[[0,defaultdict(int)] for k in range(n)] for i in range(g)] for j in range(t+1)]
for T in range(0,t):
    dpT = dp[T]
    for CUS in range(g):
        for NC in range(1,g+1):
            dpTNC = dpT[NC]
            index = bisect_left(c, NC)
            for i in range(index,n):
                if dpTNC[i][0] == 0:
                    dpT1NC = dp[T+1][NC]
                    dpTNC[i][0] = 1
                    dpTNC[i][1][NC] += 1
                    break