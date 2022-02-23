from math import pi

R,C = [int(i) for i in input().split()]
print(((R - C)**2 * pi) / (R**2 * pi) * 100)