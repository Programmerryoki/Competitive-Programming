from operator import itemgetter

T = int(input())
for a in range(T):
    N = int(input())
    ship = [[],[]]
    for b in range(N):
        line = input().split(" ")
        toy = line[0]
        quan = int(line[1])
        if toy not in ship[0]:
            ship[0].append(toy)
            ship[1].append(quan)
        else:
            ship[1][ship[0].index(toy)] += quan

    toys = [[ship[1][i],ship[0][i]] for i in range(len(ship[1]))]
    toys.sort(key=itemgetter(0),reverse = True)
    done = False
    while not done:
        toysbe = toys.copy()
        for b in range(len(toys)-1):
            if toys[b][0] == toys[b+1][0]:
                if toys[b][1] > toys[b+1][1]:
                    toys[b], toys[b + 1] = toys[b + 1], toys[b]
        if toys == toysbe:
            done = True
    print(len(ship[0]))
    for i in toys:
        print(i[1],i[0])