X,Y = input().split(".")
if 0 <= int(Y) <= 2:
    print(X+"-")
elif int(Y) <= 6:
    print(X)
else:
    print(X+"+")