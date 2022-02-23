from math import sin, cos, radians

a, b, c = [int(i) for i in input().split()]
area = 0.5 * a * b * sin(radians(c))
print(area)
print(a + b + (a**2 + b**2 - 2*a*b*cos(radians(c)))**0.5)
print(2 * area / a)