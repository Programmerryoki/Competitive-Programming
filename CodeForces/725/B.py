t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    sa = sum(a)
    if (sa / n).is_integer():
        k = 0
        m = sa // n
        for i in a:
            if i > m:
                k += 1
        print(k)
    else:
        print(-1)