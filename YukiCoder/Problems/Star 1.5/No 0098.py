from math import ceil
x,y = [int(i) for i in input().split()]
d = (x**2 + y**2)**0.5 * 2
if d.is_integer():
    d = int(d + 1)
else:
    d = ceil(d)
print(d)