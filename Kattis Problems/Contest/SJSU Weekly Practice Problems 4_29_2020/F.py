from math import log, ceil

T = int(input())
for _ in range(T):
    P,R,F = [int(i) for i in input().split()]
    y = log(F/P, R)
    if (y.is_integer()):
        print(int(y)+1)
    else:
        print(ceil(y))