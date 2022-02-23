N,K = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
pb = [(p[i] * (p[i] + 1)) / (p[i] * 2) for i in range(N)]
pr = sum(pb[:K])
m = pr
for i in range(N - K):
    pr += pb[i+K] - pb[i]
    m = max(m, pr)
print(m)