from math import pi
C = int(input())
I,O = [int(i) for i in input().split()]
V = lambda a,b: 0.25*pi**2*(a+b)*(b-a)**2
print(V(I,O)*C)