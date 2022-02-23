name = input().split()
Y = name[0]
P = name[1]
if Y[-2:] == "ex":
    print(Y+P)
elif Y[-1] in "aiou":
    print(Y[:-1]+"ex"+P)
elif Y[-1] == "e":
    print(Y+"x"+P)
else:
    print(Y+"ex"+P)