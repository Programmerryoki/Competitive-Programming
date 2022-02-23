from math import ceil
a,b,h = [int(i) for i in input().split()]
print(ceil(max((h-a)/(a-b), 0))+1)