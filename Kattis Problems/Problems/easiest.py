n = int(input())
while n != 0:
    nd = sum([int(i) for i in str(n)])
    p = 11
    while sum([int(i) for i in str(n*p)]) != nd:
        p += 1
    print(p)
    n = int(input())