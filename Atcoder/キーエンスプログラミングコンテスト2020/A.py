from math import ceil

h = int(input())
w = int(input())
n = int(input())

m = max(h,w)
print(ceil(n/m))