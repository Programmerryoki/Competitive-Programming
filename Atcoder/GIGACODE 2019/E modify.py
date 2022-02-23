N, L = [int(i) for i in input().split()]
ini = [int(i) for i in input().split()]
cars = [[0]+ini]
for a in range(N):
    cars.append([int(i) for i in input().split()])
cars.sort()
minTime = [0 for i in range(N+1)]

# cars = [position, speed of car, distance it travels]
# cc = current car
# lst = lst of all cars
# pcars = possible choices
# totalt = total time to that pos
def comb(cc, lst, pcars, totalt):
    pos = []
    cn = cc
    print("min time:", minTime)
    if minTime[cn] != 0:
        return minTime[cn]

    cc = lst[cc]
    #######################################
    print("cc",cc,"Total time:",totalt)
    for a in range(pcars[0],pcars[1]):
        print(lst[a])
    #######################################
    # check initial condition
    mi = 40075017
    if cc[0] + cc[2] >= L:
        # pos.append(totalt + (L - cc[0])/cc[1])
        pos.append((L - cc[0]) / cc[1])

    if pcars[1] - pcars[0] == 0:
        if len(pos) == 0:
            return mi
        else:
            minTime[cn] = min(pos)
            return min(pos)

    #######################################
    print(pos, "Check Possible Car\n")
    for car in range(pcars[0], pcars[1]):
        # print(lst[car])
        i = pcars[0]
        while i < len(lst) and lst[i][0] < lst[car][0]+lst[car][2]:
            i += 1
        # print([car+1, i])
        # pos.append( comb(car, lst, [car+1, i], totalt + (lst[car][0] - cc[0])/cc[1]) )
        pos.append(comb(car, lst, [car + 1, i], (lst[car][0] - cc[0])/cc[1]))
    # print("Possible :",pos,"\n")
    minTime[cn] = min(pos)
    return min(pos)


if N == 0:
    if ini[1] < L:
        print("impossible")
    else:
        print("{:.10f}".format(L/ini[0]))
else:
    i = 0
    while i < len(cars) and cars[i][0] < ini[1]:
        i += 1
    pos = comb(0, cars, [0,i], 0)
    if pos > L:
        print("impossible")
    else:
        print("{:.10f}".format(pos))