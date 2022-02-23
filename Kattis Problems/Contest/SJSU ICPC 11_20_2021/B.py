from math import acos, pi

while True:
    r,h,s = [int(i) for i in input().split()]
    if r==0 and h==0 and s==0:
        break
    ang = acos(r / h)
    tl = 2*(h**2 - r**2)**0.5 + (2*pi - 2*ang)*r
    print(f"{(tl * (100 + s) / 100):.2f}")