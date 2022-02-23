N,K = [int(i) for i in input().split()]
H = [int(input()) for i in range(N)]
H.sort()
m = float("inf")
for i in range(N - K+1):
    m = min(m, H[i+K-1] - H[i])
print(m)