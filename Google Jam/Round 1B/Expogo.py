T = int(input())
for case in range(T):
    X,Y = [int(i) for i in input().split()]
    if (X%2 == 1 and Y%2 == 1) or (X%2 == 0 and Y%2 == 0):
        print("Case #"+str(case+1)+": IMPOSSIBLE")
        continue
    move = ""
    dire = ["W","S","E","N"]
    def moves(m, c, i):
        global move
        print(m,c,i)
        if move != "":
            return
        d = 2**i
        # print(d)
        if not(d <= abs(X - c[0]) or d <= abs(Y - c[1])):
            return
        pos = [[c[0]-d, c[1]],
               [c[0], c[1]-d],
               [c[0]+d, c[1]],
               [c[0], c[1]+d]]
        # print(pos)
        for j,ac in enumerate(pos):
            if ac == [X,Y]:
                move = m+dire[j]
                return
            else:
                moves(m+dire[j], ac, i+1)

    moves("", [0,0], 0)
    print(move)