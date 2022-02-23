n = int(input())

conv = "ABCDEFGH"

for a in range(n):
    ax, ay, bx, by = input().split()
    ax, bx = conv.index(ax), conv.index(bx)
    ay, by = int(ay) - 1, int(by) - 1
    dx = bx - ax
    dy = by - ay
    if (ax + ay) % 2 != (bx + by) % 2:
        print("Impossible")
        continue

    ma = dx
    mi = dy
    if abs(dx) > abs(dy):
        ma = dx
        mi = dy

    m1 = (ma - mi)//2
    m2 = (ma + mi)//2

    midm1 = [[m1,m1],[m1,-m1]]
    midm2 = [[m2, m2], [m2, -m2]]

    for i in midm1:
        for j in midm2:
            #mid = [ax[x] + i[x] for x in range(len(i))]
            pass

    print(ax,ay,bx,by,m1,m2)