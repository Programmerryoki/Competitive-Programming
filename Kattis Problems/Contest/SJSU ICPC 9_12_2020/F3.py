from collections import deque
A,F = [int(i) for i in input().split()]
L,W = [int(i) for i in input().split()]
tile = [input() for i in range(L)]
wlist = []
start = []
end = []
for i in range(L):
    for j in range(W):
        if tile[i][j] == "W":
            wlist.append([i,j])
        elif tile[i][j] == "S":
            start = [i,j]
        elif tile[i][j] == "G":
            end = [i,j]
            wlist.append(end)