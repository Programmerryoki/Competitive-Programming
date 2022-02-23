from math import radians, degrees, sin, asin, cos, tan, atan

def area3(x,y):
    if y == 0 and x > 0:
        return 0.5 * x**2 * sin(radians(120)) * 3
    if y == 0 and x < 0:
        l = x / sin(radians(30))
        return 0.5 * l**2 * sin(radians(120)) * 3
    if x == 0:
        y = abs(y)
        l = y / tan(radians(30))
        return 0.5 * l**2 * sin(radians(120)) * 3
    if x > 0:
        y = abs(y)
        l = y / tan(radians(30)) + x
        return 0.5 * l**2 * sin(radians(120)) * 3
    y = abs(y)
    x = abs(x)
    if y == x*2:
        l = (x**2 + y**2)**0.5
        return 0.5 * l**2 * sin(radians(120)) * 3
    elif y < x*2:
        l = x / sin(radians(30))
        return 0.5 * l**2 * sin(radians(120)) * 3
    else:
        y = abs(y)
        l = y / tan(radians(30)) - x
        return 0.5 * l**2 * sin(radians(120)) * 3

def area4(x,y):
    x = abs(x)
    y = abs(y)
    return ((x+y)*2)**2 / 2

def area5(x,y):
    if y == 0 and x > 0:
        dis = x
    elif y == 0 and x < 0:
        dis = abs(x) * sin(radians(36))
    y = abs(y)
    if x > 0:
    return 0.5 * dis**0.5 * sin(radians(72)) * 5

def area6(x,y):
    x = abs(x)
    y = abs(y)
    if y == x*2:
        dis = (x**2 + y**2)**0.5
        return 0.5 * dis**2 * sin(radians(60)) * 6
    elif y == 0:
        dis = x
        return 0.5 * dis**2 * sin(radians(60)) * 6
    elif y < x*2:
        dis = y + x*2
        return 0.5 * dis**2 * sin(radians(60)) * 6
    else:
        dis = y * cos(degrees(30))
        return 0.5 * dis**2 * sin(radians(60)) * 6

def area7(x,y):

def area8(x,y):
    x = abs(x)
    y = abs(y)
    y,x = sorted([x,y])
    if y == 0:
        dis = x
    else:
        dis = (x**2 + y**2)**0.5
        ang = atan(y / x)
        A = dis * cos(ang)
        O = dis * sin(ang)
        dis = A + tan(radians(27.5)) * O
    return 0.5 * dis**2 * sin(radians(45))