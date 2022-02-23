import math
n = int(input())
for a in range(n):
    v0, theta, x1, h1, h2 = [float(i) for i in input().split()]
    xt = x1 / (v0 * math.cos(math.radians(theta)))
    y = v0 * xt * math.sin(math.radians(theta)) - 0.5 * 9.81 * xt**2
    if h1 + 1 <= y <= h2 - 1:
        print("Safe")
    else:
        print("Not Safe")