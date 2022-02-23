from math import cos, radians, pi, degrees

# radius = lambda a,b,angle: (2*((a+b)**2) - 2*((a+b)**2)*cos(angle))**0.5
def radius(a,angle):
    print("radius: ")
    A = 1 - (2 / (1 - cos(angle)))
    B = 2*a
    C = a**2
    print(a,degrees(angle),A,B,C)
    print((-B + (B**2-4*A*C)**0.5) / (2*A), (-B - (B**2-4*C)**0.5) / (2*A))
    return (-B - (B**2-4*A*C)**0.5) / (2*A)

"""
a**2 = b**2 + c**2 - 2*b*c*cos(A)
a == 2*b
b,c == a+b

4*b**2 = 2*(a+b)**2 - 2*(a+b)**2*cos(A)
2*b**2 / ((a+b)**2) = 1 - cos(A)
2*b**2 / (1 - cos(A)) = a**2 + 2*a*b + b**2
(1 - 2 / (1 - cos(A)))*b**2 + 2*a*b + a**2 = 0
x = -b +- (b**2 - 4*a*c)**0.5 / 2*a
x = -() +- (()**2 - 4*a**2)**0.5 / 2
"""

P = int(input())
for _ in range(P):
    K,N,M = map(int, input().split())
    ang = radians(360 / N)
    a,b = 1,radius(1,ang)
    dis = 1
    for _ in range(M-1):
        dis = 2*a+b
        a,b = dis, radius(dis,ang)
        print("a b: ",a,b)
    print(str(K)+" {:.3f} {:.3f}".format(b, 2*pi*b + 2*b*N))