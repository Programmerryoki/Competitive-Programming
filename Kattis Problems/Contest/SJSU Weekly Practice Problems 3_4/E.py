n, X = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p.sort()

if n == 1:
    print(1)
else:
    print(p)
    c = [p[i] + p[i-1] for i in range(1,len(p))]
    print(c)
    i = 1
    while i-1 < len(c) and c[i-1] <= n:
        i += 1
    if i == len(c):
        print(i+1)
    else:
        print(i)