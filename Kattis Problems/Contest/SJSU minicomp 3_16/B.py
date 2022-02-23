while True:
    d, N = [float(i) for i in input().split()]
    if d == 0 == N:
        break
    N = int(N)
    hives = []
    honey = [0] * N
    c = 0
    for a in range(N):
        x,y = [float(i) for i in input().split()]
        for i,b in enumerate(hives):
            if ((x - b[0])**2 + (y - b[1])**2)**0.5 < d:
                if honey[a] == 0:
                    honey[a] = 1
                    c += 1
                if honey[i] == 0:
                    honey[i] = 1
                    c += 1
        hives.append((x,y))
    print(c,"sour,",N - c,"sweet")