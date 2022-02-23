while True:
    w,l = map(int, input().split())
    if w == 0 and l == 0:
        break
    pos = [0,0]
    vpos = [0,0]
    n = int(input())
    for _ in range(n):
        x,y = input().split()
        y = int(y)
        if x == "u":
            pos[1] = min(pos[1] + y, l-1)
            vpos[1] += y
        elif x == "d":
            pos[1] = max(pos[1] - y, 0)
            vpos[1] -= y
        elif x == "l":
            pos[0] = max(pos[0] - y, 0)
            vpos[0] -= y
        elif x == "r":
            pos[0] = min(pos[0] + y, w-1)
            vpos[0] += y
    print("Robot thinks",vpos[0],vpos[1])
    print("Actually at",pos[0],pos[1])
    print()