from bisect import bisect_right

N,X = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]+[10**18+1]
ori = X
def coins(num):
    c = 0
    for i in range(N-1,-1,-1):
        if num < A[i]:
            continue
        c += num // A[i]
        num %= A[i]
    return c

ind = bisect_right(A, X)
print(ind)
money = 0
m = 0
for i in range(ind, 0, -1):
    print(money, X, A[i])
    if coins(money+A[i])+coins(money+A[i]-ori) > coins(money+(X//A[i-1])*A[i-1])+coins((money+(X//A[i-1])*A[i-1])-ori):
        money, X = money+(X//A[i-1])*A[i-1], X - (X//A[i-1]) * A[i-1]
    else:
        money += A[i]
        X = A[i] - X
    if X == 0:
        break
print(money)
m = min(coins(ori), coins(money) + coins(money - ori))
print(m)