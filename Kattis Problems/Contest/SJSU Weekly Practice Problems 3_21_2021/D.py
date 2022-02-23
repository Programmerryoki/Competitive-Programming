from math import log2, ceil

n = int(input())
days = ceil(log2(n))
print(days+1)