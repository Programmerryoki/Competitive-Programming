while True:
    n,m = [int(i) for i in input().split()]
    if n == m == 0:
        break

    best = [-1,-1,-1]
    for _ in range(n):
        a,b = [int(i) for i in input().split()]
        if a > m:
            continue
        elif a == 0:
            continue
        else:
            if best != [-1,-1,-1]:
                if b/a < best[2]:
                    best = [a,b,b/a]
                elif b/a == best[2]:
                    if a > best[0]:
                        best = [a,b,b/a]
            else:
                best = [a,b,b/a]
    if best != [-1,-1,-1]:
        print("Buy",best[0],"tickets for $"+str(best[1]))
    else:
        print("No suitable tickets offered")