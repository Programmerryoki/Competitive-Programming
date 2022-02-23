from math import ceil
A,B,C = [int(i) for i in input().split()]
if A*60 < B:
    print(-1)
else:
    print(ceil(C*60*60 / (A*60 - B)))