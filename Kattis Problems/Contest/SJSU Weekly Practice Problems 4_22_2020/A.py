n = int(input())
S = [int(input()) for i in range(n)]
S.sort(reverse=True)
# print([(4/5)**i*S[i] for i in range(n)])
sg = sum([(4/5)**i*S[i] for i in range(n)])/5
print(sg)
g = [0]*n
for i in range(n):
    total = 0
    for j,s in enumerate(S[:i]+S[i+1:]):
        total += ((4/5)**j)*s
    g[i] = total / 5
print(sum(g)/(n))