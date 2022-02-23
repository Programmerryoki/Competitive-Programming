n = int(input())
for _ in range(n):
    fl = input().split()
    nl = input().split()
    if len(fl) != len(nl):
        print("-")
        continue
    dictf = {}
    dicty = {}
    pos = True
    for i in range(len(fl)):
        fl0 = fl[i][0]
        nl0 = nl[i][0]
        if fl0 == "<" and nl0 == "<":
        elif fl0 == "<":
        elif nl0 == "<":
        else:
            pos = False