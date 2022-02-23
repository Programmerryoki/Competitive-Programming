from math import log10

a,b,c = [int(i) for i in input().split()]
print("Yes" if a < c**b else "No")