T = int(input())
for _ in range(T):
    a,b,n = [int(i) for i in input().split()]
    c = 0
    while a <= n and b <= n:
        if a > b:
            b += a
        else:
            a += b
        c += 1
    print(c)