X,Y,Z = [int(i) for i in input().split()]
c = Y * Z / X
print(int(c) if not c.is_integer() else int(c) - 1)