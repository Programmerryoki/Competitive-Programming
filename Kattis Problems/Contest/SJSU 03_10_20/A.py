from math import sin, cos, radians

t = int(input())
for _ in range(t):
    x = 0
    y = 0
    ang = 0
    n = int(input())
    for b in range(n):
        cmd = input()
        if cmd[0] == "f":
            nn = int(cmd.split()[1])
            x += nn * sin(radians(ang))
            y += nn * cos(radians(ang))
        elif cmd[0] == "l":
            ang += int(cmd.split()[1])
        elif cmd[0] == "b":
            nn = int(cmd.split()[1])
            x += nn * sin(radians(-ang))
            y += nn * cos(radians(-ang))
        else:
            ang -= int(cmd.split()[1])
    print(round((x**2 + y**2)**0.5))