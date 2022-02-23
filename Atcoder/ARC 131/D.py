N,M,D = [int(i) for i in input().split()]
R = [int(i) for i in input().split()]
S = [int(i) for i in input().split()]
maxscore = 0
ts = S[0]
an = 0.5
cur = 0
for i in range(1,M):
    n = min((R[i] - cur) // D, -(-(N - 2*an)//2))
    print(i,n,an,cur,ts)
    if (an+n)*2 >= N:
        ts += (n - ((an+n)*2-N)/2) * S[i-1]
        break
    ts += n * S[i-1]
    cur += n * D
    an += n
print(ts*2)
maxscore = max(maxscore, 2*ts-S[0])
ts = 0
an = 0
cur = -D/2
for i in range(1,M):
    n = min((R[i] - cur) // D, -(-(N - 2*an)//2))
    print(i,n,an,cur,ts)
    if (an+n)*2 >= N:
        ts += (n - ((an+n)*2-N)/2) * S[i-1]
        break
    ts += n * S[i-1]
    cur += n * D
    an += n
print(ts*2)
maxscore = max(maxscore, 2*ts)
print(maxscore)