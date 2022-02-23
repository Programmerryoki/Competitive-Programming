A,B,X,Y = [int(i) for i in input().split()]
mul = min(X/A, Y/B)
print((A+B)*mul)