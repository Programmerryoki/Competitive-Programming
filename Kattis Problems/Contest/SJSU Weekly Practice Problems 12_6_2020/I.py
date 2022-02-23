from math import acos, pi

while True:
    r,h,s = map(int, input().split())
    if [r,h,s].count(0) == 3:
        break
    tl = 2*(h**2 - r**2)**0.5 + ((2 * (pi - acos(r / h))) / (2*pi)) * 2 * r * pi
    print("{:.2f}".format(round(tl * (100 + s) / 100, 2)))