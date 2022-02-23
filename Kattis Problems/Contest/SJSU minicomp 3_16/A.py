from math import acos, pi

n = int(input())
for _ in range(n):
    D, d, s = [float(i) for i in input().split()]
    a = (D - d)/2
    c = d + s
    ss = (a**2 + a**2 - c**2) / (2 * a * a)
    ang = acos(ss)
    print(int(2 * pi // ang))