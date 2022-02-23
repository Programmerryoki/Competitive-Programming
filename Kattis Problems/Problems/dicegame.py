gd = [int(i) for i in input().split()]
ed = [int(i) for i in input().split()]
g = (sum([i for i in range(gd[0],gd[1]+1)]) / (gd[1] - gd[0] + 1)) + (sum([i for i in range(gd[2],gd[3]+1)]) / (gd[3] - gd[2] + 1))
e = (sum([i for i in range(ed[0],ed[1]+1)]) / (ed[1] - ed[0] + 1)) + (sum([i for i in range(ed[2],ed[3]+1)]) / (ed[3] - ed[2] + 1))
if g > e:
    print("Gunner")
elif g < e:
    print("Emma")
else:
    print("Tie")