N = int(input())
leng = [0]*N
ma = 0
for i in range(N):
    a,b = [int(j) for j in input().split()]
    leng[i] = a + 4*b
    ma = max(ma, a + 4*b)
sl = sum([i&1 for i in leng])
if sl == 0 or sl == N:
    print(sum([(ma - i)//2 for i in leng]))
else:
    print(-1)