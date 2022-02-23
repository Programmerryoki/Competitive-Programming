def wise(c1, c2, c3) -> int:
    vx = c2[0] - c1[0]
    vy = c2[1] - c1[1]
    if vx == 0:
        if vy > 0:
            if c2[0] == c3[0]:
                return -1
            elif c2[0] > c3[0]:
                return 0
            else:
                return 1
        else:
            if c2[0] == c3[0]:
                return -1
            elif c2[0] > c3[0]:
                return 1
            else:
                return 0
    elif vy == 0:
        if vx > 0:
            if c2[1] == c3[1]:
                return -1
            elif c2[1] > c3[1]:
                return 0
            else:
                return 1
        else:
            if c2[1] == c3[1]:
                return -1
            elif c2[1] > c3[1]:
                return 1
            else:
                return 0


n = int(input())
while n != 0:
    vertices = []
    for a in range(n):
        coor = [int(i) for i in input().split()]
        vertices.append(coor)

    vx = [vertices[i][0] for i in range(n)]
    vy = [vertices[i][1] for i in range(n)]
    area = 0
    ax = 0
    ay = 0
    for a in range(n):
        area += vx[a]*vy[(a+1)%n]
        ax += vx[a] * vy[(a + 1)%n]
        area -= vy[a]*vx[(a+1)%n]
        ay += vy[a]*vx[(a+1)%n]
    area /= 2
    print(ax, ay)

    cw = wise(vertices[0], vertices[1], vertices[2])
    i = 1
    while i < n - 2 and cw == -1:
        cw = wise(vertices[i], vertices[i+1], vertices[i+2])
        i += 1

    if cw == 1:
        print("CW {:.1f}".format(area))
    elif cw == 0:
        print("CCW {:.1f}".format(area))
    else:
        print("Error {:.1f}".format(area))


    n = int(input())