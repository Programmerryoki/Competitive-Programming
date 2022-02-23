while True:
    try:
        n,*rest = [int(i) for i in input().split()]
    except:
        break
    dif = []
    for i in range(n-1):
        dif.append(abs(rest[i] - rest[i+1]))
    dif.sort()
    for i in range(n-1):
        if dif[i] != i+1:
            print("Not jolly")
            break
    else:
        print("Jolly")