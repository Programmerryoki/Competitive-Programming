from math import gcd
lcm = lambda x,y: (x*y)//gcd(x,y)
A,B,C,D = [int(i) for i in input().split()]
print(B - A + 1 - (B//C - (A-1)//C) - (B//D - (A-1)//D) + (B//lcm(C,D) - (A-1)//lcm(C,D)))