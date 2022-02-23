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
moveelsa = [[1,0],[-1,0],[0,1],[0,-1]]
movefather = [[1,0],[-1,0],[0,1],[0,-1]]
while True:
    if queelsa:
        eque = queelsa
        seen = set()
        ed = 1
        neque = deque()
        while ed <= A:
            nnque = deque()
            while eque:
                ei,ej = eque.popleft()
                for edx,edy in moveelsa:
                    ex,ey = edx+ei, edy+ej
                    if 0 <= ex < L and 0 <= ey < W:
                        if tile[ex][ey] != "B" and elsa[ex][ey] == float("inf"):
                            string = str(ex) + " " + str(ey)
                            if string in seen:
                                continue
                            seen.add(string)
                            nnque.append([ex, ey])
                            neque.append([ex, ey])
            ed += 1
            eque = nnque
        for i,j in neque:
            elsa[i][j] = d+1

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
    # print(queelsa,neque)
    # print(quefather,newfather)
    elsaend = (elsa[end[0]][end[1]] != float("inf"))
    fatherend = (father[end[0]][end[1]] != float("inf"))
    if not neque and not newfather and not queelsa and not quefather and not elsaend and not fatherend:
        print("NO WAY")
        exit()
    if not elsaend and not fatherend:
        queelsa = neque
        quefather = newfather
        continue
    if elsaend and fatherend and (elsa[end[0]][end[1]] == father[end[0]][end[1]]):
        print("SUCCESS")
        exit()
    elif elsaend:
        print("GO FOR IT")
        exit()
    elif fatherend:
        print("NO CHANCE")
        exit()

    if elsaend and fatherend:
        if elsa[end[0]][end[1]] == father[end[0]][end[1]]:
            print("SUCCESS")
        elif elsa[end[0]][end[1]] < father[end[0]][end[1]]:
            print("GO FOR IT")
        elif elsa[end[0]][end[1]] > father[end[0]][end[1]]:
            print("NO CHANCE")
        exit()
    else:
        queelsa = newelsa
        quefather = newfather