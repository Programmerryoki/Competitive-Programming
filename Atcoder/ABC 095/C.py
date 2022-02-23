A,B,C,X,Y = [int(i) for i in input().split()]
if A + B < C * 2:
    print(A*X + B*Y)
else:
    p1 = min(X,Y) * C * 2 + (X - min(X,Y))*A + (Y - min(X,Y))*B
    p2 = max(X,Y) * C * 2
    print(min(p1, p2))