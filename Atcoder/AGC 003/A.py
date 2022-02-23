S = input()
dir = [0]*4
move = "NWSE"
for i in S:
    dir[move.index(i)] += 1
p1 = (dir[0] > 0 and dir[2] > 0) or (dir[0] == 0 and dir[2] == 0)
p2 = (dir[1] > 0 and dir[3] > 0) or (dir[1] == 0 and dir[3] == 0)
print("Yes" if p1 and p2 else "No")