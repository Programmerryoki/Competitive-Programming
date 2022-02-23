n,N = map(int, input().split())
ant1 = [[i, 1] for i in input()[::-1]]
ant2 = [[i, -1] for i in input()]
ant = ant1 + ant2
for i in range(int(input())):
    na = []
    j = 0
    while j < len(ant) - 1:
        if ant[j][1] == 1 and ant[j+1][1] == -1:
            na.append(ant[j+1])
            na.append(ant[j])
            j += 2
        else:
            na.append(ant[j])
            j += 1
    if j < len(ant):
        na.append(ant[j])
    ant = na
print("".join([i[0] for i in ant]))