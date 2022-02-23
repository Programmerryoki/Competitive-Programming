line = input()
# WhiteC, LowerL, UpperL, Symbol
ratio = [0, 0, 0, 0]
for a in line:
    w = ord(a)
    if w == ord("_"):
        ratio[0] += 1
    elif ord("a") <= w <= ord("z"):
        ratio[1] += 1
    elif ord("A") <= w <= ord("Z"):
        ratio[2] += 1
    else:
        ratio[3] += 1
length = float(len(line))
for a in ratio:
    print(a/length)