from math import sin, cos, pi, atan, degrees

T = int(input())
L,X,Y = [int(i) for i in input().split()]
z = lambda t: -L/2 * cos(2 * t * pi / T) + L/2
y = lambda t: -L/2 * sin(2 * t * pi / T)
Q = int(input())
for _ in range(Q):
    E = int(input())
    dx = abs(X)
    dy = abs(Y - y(E))
    dz = abs(z(E))
    dxy = (dx**2 + dy**2)**0.5
    print(degrees(atan(dz / dxy)))