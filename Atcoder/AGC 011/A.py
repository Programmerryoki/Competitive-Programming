N,C,K = [int(i) for i in input().split()]
T = [int(input()) for _ in range(N)]
nbus = 1
cus = 0
t = T[0]
for i in range(N):
    if T[i] <= t + K and cus + 1 <= C:
        cus += 1
    else:
        if cus + 1 == C and i+1 < N:
            t = T[i+1]
        else:
            t = T[i]
        cus = 0
        nbus += 1
print(nbus)