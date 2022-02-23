T = int(input())
for case in range(T):
    R,C = [int(i) for i in input().split()]
    dance = [[int(i) for i in input().split()] for j in range(R)]
    ilc = 0
    while True:
        # for row in dance:
        #     print(row)
        # print()

        il = 0
        elim = []
        for i in range(R):
            for j in range(C):
                if dance[i][j] == -1:
                    continue

                al = j - 1
                while 0 <= al and dance[i][al] == -1:
                    al -= 1
                ar = j + 1
                while ar < C and dance[i][ar] == -1:
                    ar += 1
                au = i - 1
                while 0 <= au and dance[au][j] == -1:
                    au -= 1
                ad = i + 1
                while ad < R and dance[ad][j] == -1:
                    ad += 1
                # print([i, j, dance[i][j]], al, ar, au, ad)
                s = 0
                n = 0
                if 0 <= al:
                    s += dance[i][al]
                    n += 1
                if ar < C:
                    s += dance[i][ar]
                    n += 1
                if 0 <= au:
                    s += dance[au][j]
                    n += 1
                if ad < R:
                    s += dance[ad][j]
                    n += 1

                if n != 0:
                    if dance[i][j]*n < s:
                        # print("elim")
                        elim.append([i,j])
                il += dance[i][j]
        # print(il)
        ilc += il
        if len(elim) == 0:
            break
        for x,y in elim:
            dance[x][y] = -1
    print("Case #"+str(case+1)+":",ilc)