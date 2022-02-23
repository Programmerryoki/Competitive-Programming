S = input()
e,w = 0,0
for s in S:
    if s == "O":
        e += 1
        w = 0
    else:
        e = 0
        w += 1
    if e == 3 or w == 3:
        print("East" if e == 3 else "West")
        break
else:
    print("NA")