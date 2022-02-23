while True:
    d,N = [float(i) for i in input().split()]
    if d == N == 0:
        break
    N = int(N)
    fight = [0]*N
    hives = []
    for h in range(N):
        x,y = [float(i) for i in input().split()]
        for i,j in enumerate(hives):
            a,b = j
            if ((x-a)**2 + (y-b)**2)**0.5 <= d:
                fight[i] = 1
                fight[h] = 1
        hives.append([x,y])
    print(fight.count(1),"sour,",fight.count(0),"sweet")