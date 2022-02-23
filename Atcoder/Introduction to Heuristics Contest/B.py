D = int(input())
C = [int(i) for i in input().split()]
scores = [[int(i) for i in input().split()] for j in range(D)]
t = [int(input()) for i in range(D)]

ans = []
S = 0
last = [0]*26
for d in range(1,D+1):
    S += scores[d-1][t[d-1]-1]
    last[t[d-1]-1] = d
    for i in range(26):
        S -= C[i] * (d - last[i])
    ans.append(S)
print("\n".join(map(str, ans)))