from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N,M = [int(i) for i in input().split()]
    A = 0
    MA = -float("inf")
    pv = 0
    for j in range(N):
        x,y = [int(i) for i in input().split()]
        s = ((y+1)*y // 2) * x + pv * y
        A += s
        pv = x * y
        print(A, x, y, s)
        if A > MA:
            MA = A
        if j == 0:
            MA = max(MA, x)
    print(MA)