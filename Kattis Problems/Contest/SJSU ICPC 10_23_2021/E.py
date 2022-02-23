while True:
    L,R = [int(i) for i in input().split()]
    if L == 0 and R == 0:
        break
    divider = [int(i) for i in input().split()]
    minarea = 0
    mid = -(-abs(L)//2)
    print("mid",mid)
    j = 0
    h = 0
    tf = 0
    for i in range(len(divider)):
        print(i, divider[i], tf, h)
        if i < mid:
            if divider[i] >= h:
                tf += divider[i]
                h = divider[i]
                j = i
        elif h <= divider[i]:
            tf += h * (i - j - 1)
            break
    else:
        tf = float("inf")
    print("tf",tf)
    j = len(divider)-1
    h = 0
    tb = 0
    for i in range(len(divider)-1,-1,-1):
        print(i, divider[i], tb, h)
        if i >= mid:
            if divider[i] >= h:
                tb += divider[i]
                h = divider[i]
                j = i
        elif h <= divider[i]:
            tb += h * (j - i - 1)
            break
    else:
        tb = float("inf")
    print("tb", tb)
    print(min(tf, tb) * 2)