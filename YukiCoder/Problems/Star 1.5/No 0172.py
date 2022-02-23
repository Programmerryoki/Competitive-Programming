from math import ceil
x,y,r = [int(i) for i in input().split()]
print(ceil(abs(x) + abs(y) + 2**0.5 * r))