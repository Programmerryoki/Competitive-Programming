from math import cos, radians, pi, sin

N = int(input())
for _ in range(N):
    n,l,d,g = [int(i) for i in input().split()]
    c = 360/n
    a = (l**2/(2*(1-cos(radians(c)))))**0.5
    # print(0.5*a**2*sin(radians(c))*n , n*(d*g*l) , (d*g)**2*pi)
    print(0.5*a**2*sin(radians(c))*n + n*(d*g*l) + (d*g)**2*pi)