from math import ceil
X = int(input())
Y = int(input())
L = int(input())
# print(X/L, ceil(X/L), Y/L, ceil(Y/L), abs(ceil(X/L)) + abs(ceil(Y/L)))
if X!=0 and Y!=0:
    if X > 0 and Y > 0:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)) + 1)
    elif X > 0 and Y < 0:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)) + 2)
    elif X < 0 and Y > 0:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)) + 1)
    elif X < 0 and Y < 0:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)) + 2)
else:
    if X == 0 and Y == 0:
        print(0)
    elif Y < 0:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)) + 2)
    elif Y == 0:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)) + 1)
    else:
        print(ceil(abs(X/L)) + ceil(abs(Y/L)))