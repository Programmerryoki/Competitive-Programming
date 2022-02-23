# given number in P, find next number in Q that is multiple of P
# from the first index until the multiple of P
#   iterate through and find its multiple
#   if its index is less than first, change first index
# repeat until reach end

N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]
mn = 0
nxt = 0
while nxt < N:
    for ind in range(nxt, N):
        if Q[ind] % P[nxt] == 0:
            break
    for i in range(nxt, ind):
        for j in range(nxt, N):
            if Q[j] % P[i] == 0:
                break
        if j < ind:
            ind = j
    nxt = ind + 1
    if nxt >= N:
        break
    mn += 1
    print(nxt)
print(mn)