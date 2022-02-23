A,B,C = [int(i) for i in input().split()]
if (-(-A // C)) * C <= B:
    print((-(-A // C)) * C)
else:
    print(-1)