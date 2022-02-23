N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
ans = N - sum(A)
if ans >= 0:
    print(ans)
else:
    print(-1)