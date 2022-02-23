from math import cos,radians,sin

# c = lambda a,b,C: (a**2 + b**2 - 2*a*b*cos(radians(C)))**0.5
t = int(input())
for _ in range(t):
    ncmd = int(input())
    x, y = 0, 0
    dir = 0
    for _ in range(ncmd):
        d, l = input().split()
        l = int(l)
        if d == "lt":
            dir = (dir + 360 - l)%360
        elif d == "rt":
            dir = (dir + l)%360
        elif d == "fd":
            x += l*sin(radians(dir))
            y += l*cos(radians(dir))
        else:
            x -= l*sin(radians(dir))
            y -= l*cos(radians(dir))
    print(round((x**2 + y**2)**0.5))