X = input()
if int(X[X.index(".")+1]) <= 4:
    print(int(X[:X.index(".")]))
else:
    print(int(X[:X.index(".")]) + 1)