A,F = [int(i) for i in input().split()]
L,W = [int(i) for i in input().split()]

map = []
start = [0,0]
end = [0,0]
for i in range(L):
    line = input()
    t = [0]*W
    for j,a in enumerate(line):
        if a == "W":
            t[j] = 1
        elif a == "S":
            start = [i,j]
            t[j] = 2
        elif a == "G":
            end = [i,j]
            t[j] = 3
    map.append(t)
mapa = [[-1]*W for i in range(L)]
mapf = [[-1]*W for i in range(L)]

