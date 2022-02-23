from math import log2, ceil
H = int(input())
print(2**(ceil(log2(H))+1 if log2(H).is_integer() else ceil(log2(H))) - 1)