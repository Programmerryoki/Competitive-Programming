from math import radians, degrees, sin, asin, cos, tan, atan

def area3(x,y) -> int:
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

def area4(x,y) -> int:
    x = abs(x)
    y = abs(y)
    return ((x+y)*2)**2 / 2

def area5(x,y) -> int:
    if y == 0 and x > 0:
        dis = x
        return 0.5 * dis**0.5 * sin(radians(72)) * 5
    y = abs(y)
    ty = tan(radians(36)) * -x
    if x < 0 and y <= ty:
        dis = abs(x) * sin(radians(36))
    elif x > 0 and y <= tan(radians(72)) * x:
        dis = x + (y / tan(radians(54)))
    elif x < 0:
        dis =
    return 0.5 * dis**0.5 * sin(radians(72)) * 5

def area6(x,y) -> int:
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

def area7(x,y) -> int:
    return 0

def area8(x,y) -> int:
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

def main():
    n = int(input())
    points = [[int(i) for i in input().split()] for j in range(n)]
    meths = [area3, area4, area5, area6, area7, area8]
    res = []
    for i,method in enumerate(meths):
        pm = [method(*i) for i in points]
        ma = max(pm)
        mi = min(pm)
        ans = mi / ma
        res.append([i+3, ans])
    print(" ".join(str, max(res, key=lambda x: x[1])))

if __name__ == "__main__":
    main()