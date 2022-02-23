from collections import deque

A,F = [int(i) for i in input().split()]
L,W = [int(i) for i in input().split()]
elsa = [[float("inf") for i in range(W)] for j in range(L)]
father = [[float("inf") for i in range(W)] for j in range(L)]
tile = [0]*L
start = []
end = []
for i in range(L):
    line = input()
    if "S" in line:
        start = [i,line.index("S")]
    if "G" in line:
        end = [i, line.index("G")]
    tile[i] = line
# print(start,end)
elsa[start[0]][start[1]] = 0
father[start[0]][start[1]] = 0

d = 0
queelsa = deque([start])
quefather = deque([start])
moveelsa = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
movefather = [[1,0],[-1,0],[0,1],[0,-1]]
while True:
    newelsa = deque()
    while queelsa:
        i,j = queelsa.popleft()
        for mx, my in moveelsa:
            for mul in range(1,A+1):
                for ax in range(mul+1):
                    dx = ax * mx
                    dy = (A - ax) * my
                    x,y = dx+i, dy+j
                    if 0 <= x < L and 0 <= y < W:
                        if tile[x][y] == "G":
                            elsa[x][y] = d+1
                            queelsa = deque()
                            newelsa = deque()
                            break
                        if tile[x][y] != "B" and elsa[x][y] == float("inf"):
                            elsa[x][y] = d+1
                            newelsa.append([x,y])
    newfather = deque()
    while quefather:
        i,j = quefather.popleft()
        for dx,dy in movefather:
            for mul in range(1,F+1):
                x,y = dx*mul+i, dy*mul+j
                if 0 <= x < L and 0 <= y < W:
                    if tile[x][y] == "G":
                        father[x][y] = d+1
                        quefather = deque()
                        newfather = deque()
                        break
                    if tile[x][y] != "B" and father[x][y] == float("inf"):
                        father[x][y] = d+1
                        newfather.append([x,y])
    d += 1

    # print()
    # for i in elsa:
    #     print(i)
    # print()
    # for i in father:
    #     print(i)
    # print()
    # print(queelsa,newelsa)
    # print(quefather,newfather)
    elsaend = (elsa[end[0]][end[1]] != float("inf"))
    fatherend = (father[end[0]][end[1]] != float("inf"))
    if not newelsa and not newfather and not queelsa and not quefather and not elsaend and not fatherend:
        print("NO WAY")
        exit()
    if elsaend and fatherend and (elsa[end[0]][end[1]] == father[end[0]][end[1]]):
        print("SUCCESS")
        exit()
    elif elsaend:
        print("GO FOR IT")
        exit()
    elif fatherend:
        print("NO CHANCE")
        exit()
    else:
        queelsa = newelsa
        quefather = newfather
        continue