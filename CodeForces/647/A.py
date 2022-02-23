t = int(input())
for _ in range(t):
    a,b = [int(i) for i in input().split()]
    if a > b:
        c = 0
        for i in range(3,0,-1):
            while a > b and (a/(2**i)).is_integer():
                a //= 2**i
                c += 1
        if a == b:
            print(c)
        else:
            print(-1)
    elif a < b:
        c = 0
        while a < b:
            a *= 2
            c += 1
        if a == b:
            t = 0
            t += c//3
            c %= 3
            t += c//2
            c %= 2
            t += c
            print(t)
        else:
            print(-1)
    else:
        print(0)