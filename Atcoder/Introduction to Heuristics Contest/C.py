D = int(input())
C = [int(i) for i in input().split()]
scores = [[int(i) for i in input().split()] for j in range(D)]
t = [int(input()) for i in range(D)]
DC = [0]*26

def calcScore(t):
    score = []
    S = 0
    last = [0]*26
    for d in range(1,D+1):
        S += scores[d-1][t[d-1]-1]
        last[t[d-1]-1] = d
        for i in range(26):
            S -= C[i] * (d - last[i])
            DC[i] += (d - last[i])
        score.append(S)
    return score[-1]

ans = []
M = int(input())
for _ in range(M):
    d,q = [int(i) for i in input().split()]
    t[d-1] = q
    ans.append(calcScore(t))
    # dif = scores[d-1][q-1] - scores[d-1][t[d-1]-1]
    # difc = C[q-1] - C[t[d-1]-1]
    # for i in range(d-1, D):
    #     score[i] += dif + difc * (i - d + 2)
    # ans.append(score[-1])
print("\n".join(map(str, ans)))