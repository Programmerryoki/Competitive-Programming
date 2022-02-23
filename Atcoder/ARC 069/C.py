N,M = [int(i) for i in input().split()]
if N >= M:
    print(M//2)
    exit()
ans = 0
ans = max(ans, N + (M - N*2) // 4)
print(ans)