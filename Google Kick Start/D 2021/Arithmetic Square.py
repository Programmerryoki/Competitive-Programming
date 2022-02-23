from collections import defaultdict

T = int(input())
for case in range(T):
    grid = [[int(i) for i in input().split()] for j in range(3)]
    poscases = defaultdict(int)
    arithnum = 0
    def operate(lst):
        global arithnum, poscases
        lst.sort()
        if len(lst) != 3:
            dif = (lst[1] - lst[0])
            poscases[lst[1] + dif] += 1
            poscases[lst[0] - dif] += 1
            if not dif&1:
                poscases[lst[0] + dif//2] += 1
        else:
            if lst[0] - lst[1] == lst[1] - lst[2]:
                arithnum += 1

    for i in range(3):
        # row
        lst = list(grid[i])
        operate(lst)
    operate([grid[0][0], grid[1][0], grid[2][0]])
    operate([grid[0][1], grid[2][1]])
    operate([grid[0][2], grid[1][1], grid[2][2]])
    operate([grid[0][0], grid[2][2]])
    operate([grid[0][2], grid[2][0]])

    def check(num):
        G = [grid[0][:],
             [grid[1][0], num, grid[1][1]],
             grid[2][:]]
        # print(G)
        ar = 0
        for i in range(3):
            lst = list(G[i])
            # print(lst)
            lst.sort()
            if not (lst[2]-lst[0])&1 and (lst[2]+lst[0]) // 2 == lst[1]:
                ar += 1
            lst = [G[j][i] for j in range(3)]
            # print(lst)
            lst.sort()
            if not (lst[2]-lst[0])&1 and (lst[2]+lst[0]) // 2 == lst[1]:
                ar += 1
        lst = [G[i][i] for i in range(3)]
        # print(lst)
        lst.sort()
        if not (lst[2]-lst[0])&1 and (lst[2]+lst[0]) // 2 == lst[1]:
            ar += 1
        lst = [G[i][3-i-1] for i in range(3)]
        # print(lst)
        lst.sort()
        if not (lst[2]-lst[0])&1 and (lst[2]+lst[0]) // 2 == lst[1]:
            ar += 1
        return ar

    # print(poscases.keys())
    maximum = 0
    for num in poscases:
        m = check(num)
        # print(num, m)
        if m > maximum:
            maximum = m
    print(f"Case #{case+1}: {maximum}")
    # print(f"Case #{case+1}: {min(8, arithnum + max(poscases.values()))}")