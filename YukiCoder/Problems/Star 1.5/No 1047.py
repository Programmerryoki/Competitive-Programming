A,B = [int(i) for i in input().split()]
if B == 0:
    print(1)
else:
    if A >= 0:
        print(-1)
    else:
        c = 1
        N = B
        while N != 0:
            if N > B:
                print(-1)
                break
            N = A*N + B
            c += 1
        else:
            print(c)