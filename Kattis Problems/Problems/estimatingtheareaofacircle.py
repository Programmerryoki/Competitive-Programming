from math import pi

while True:
    r,m,c = [float(i) for i in input().split()]
    if r == m == c == 0:
        break

    print(pi * r**2, (2*r)**2 * c / m)