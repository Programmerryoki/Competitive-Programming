C = int(input())
for case in range(1,C+1):
    N,T = map(int, input().split())
    E = int(input())
    emp = [[int(i) for i in input().split()] for j in range(E)]
    emp = list(filter(lambda x: x[0] != T, emp))
    count = [[0,[]] for i in range(N)]
    for town,car in emp:
        count[town-1][0] += 1
        count[town-1][1].append(car)
    # print(count)
    ncar = [0]*N
    imp = False
    for j,[nppl,cars] in enumerate(count):
        cars.sort(reverse=True)
        if sum(cars) < nppl:
            imp = True
            break
        # print(nppl,cars)
        s = 0
        i = 0
        while i < len(cars):
            s += cars[i]
            if s >= nppl:
                i += 1
                break
            i += 1
        ncar[j] += i

    print("Case #"+str(case)+":","IMPOSSIBLE" if imp else " ".join(map(str, ncar)))