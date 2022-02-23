N,W = map(int, input().split())
ppl = [[int(i) for i in input().split()] for j in range(N)]
mt = max([i[1] for i in ppl])
minute = [0]*(mt+1)
for s,t,p in ppl:
    minute[s] += p
    minute[t] -= p
water = 0
for i in minute:
    water += i
    if water > W:
        print("No")
        exit()
print("Yes")