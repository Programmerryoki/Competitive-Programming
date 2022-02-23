while True:
    n, x = [int(i) for i in input().split()]
    if n == x == 0:
        break

    c = 0
    for a in range(1,n):
        for b in range(a+1, n+1):
            num = x - a - b
            if n >= num > b:
                c += 1
                # print(a,b,num)
            elif b > num:
                break
    print(c)