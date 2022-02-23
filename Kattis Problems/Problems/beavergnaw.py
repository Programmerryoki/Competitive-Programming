import math


D, V = [float(i) for i in input().split()]
while D and V:
    print((D**3 - (6 * V / math.pi))**(1/3))
    D, V = [float(i) for i in input().split()]


"""
volume of D: (D/2.0)**2 * math.pi * D
volume of cone D: (D / 2.0)**2 * math.pi * D * 2 / 3
volume of d:      (d / 2.0)**2 * math.pi * d * 2 / 3

V = volume of cone D - volume of d

"""