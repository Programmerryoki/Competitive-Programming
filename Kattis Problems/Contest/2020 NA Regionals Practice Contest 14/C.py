n = int(input())
a = [int(i) for i in input().split()]
al = [[i,j+1] for j,i in enumerate(a) if i != 0]
moves = []
addMove = lambda x,y: moves.append(str(x)+" "+str(y))
while len(al) > 1:
    # print(al)
    al.sort(key = lambda x: (-x[0]))
    al0 = al[0]
    al1 = al[1]
    m = min(al0[0], al1[0])
    if len(al) >= 3:
        al2 = al[2]
        m = min(max(1, (al0[0]+al1[0]-al2[0]) // 2), m)
    # print(m)
    for i in range(m):
        addMove(al0[1], al1[1])
    al0[0] -= m
    al1[0] -= m
    if al0[0] == 0:
        al.remove(al0)
    if al1[0] == 0:
        al.remove(al1)
if not len(al):
    print("yes")
    print("\n".join(moves))
    exit()
print("no")