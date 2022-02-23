from math import cos, radians

A,B,H,M = [int(i) for i in input().split()]
ans = lambda a,b,c: (a**2 + b**2 - 2*a*b*cos(radians(c)))**0.5
ang = min(abs(H*30 + M*0.5 - M*6), 360 - abs(H*30 + M*0.5 - M*6))
print(ans(A,B,ang))