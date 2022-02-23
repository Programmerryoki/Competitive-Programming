import math
n = N = int(input())

def trend(n):
    c = 0
    n = str(n)
    i = len(n)-1
    while n[i] == "0":
        c += 1
        i -= 1
    return c

if n%2 == 1:
    print(0)
else:
    c = 10
    t = 0
    i = 0
    while c <= n:
        i = len(str(c))
        if i%2==0:
            t += (i-1)*n//c
        else:
            t += (i-1)*n//c
        # t += n//c
        c *= 10
    print(t)
    c = 50
    # while c <= n:
    #     i = math.log(c, 50)
    #     if i%2 == 1:
    #         t += (i-1)*n // c
    #     else:
    #         t -= (i-1)*n // c
    #     c *= 5
    # print(t)
    # num = 1
    # for a in range(N,0,-2):
    #     num *= a
    #     print(a, trend(num))
    # print(num)