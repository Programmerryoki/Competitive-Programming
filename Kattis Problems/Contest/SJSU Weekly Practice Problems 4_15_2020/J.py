ranks = [10000,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,3,3,3,3,3,2,2,2,2,2]
rank = ["Legend"]+[str(i) for i in range(1,26)]
games = input()
S = 0
R = 25
cw = 0
for i in games:
    # print(S,R,cw)
    if i == "W":
        cw += 1
        if cw >= 3 and R > 5:
            S += 2
        else:
            S += 1

        if S > ranks[R]:
            if S - ranks[R] == 2:
                S = 2
                R -= 1
            else:
                S = 1
                R -= 1
    else:
        cw = 0
        if 0 < R <= 20:
            S -= 1
        if S < 0:
            S = ranks[R+1]-1
            R += 1
            if R > 20:
                S = 0
                R = 20
# print(S,R,cw)
print(rank[R])