from math import ceil

R,X,Y = map(int, input().split())
dis = (X**2 + Y**2)**0.5
if (dis / R).is_integer():
    print(ceil(dis / R))
else:
    ans = ceil(dis / R)
    print(max(2, ans))