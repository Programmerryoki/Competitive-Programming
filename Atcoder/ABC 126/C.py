from math import log2

N,K = [int(i) for i in input().split()]
prob = 0
for i in range(1,N+1):
    j = 0
    while 2**(j) * i < K:
        j += 1
    prob += (1/N) * (0.5)**j
    # print((1/N) * (0.5)**j, j)
print(prob)