X,Y,A,B = [int(i) for i in input().split()]
exp = -1
while X < Y:
    exp += 1
    X = min(X*A, X+B)
print(exp)