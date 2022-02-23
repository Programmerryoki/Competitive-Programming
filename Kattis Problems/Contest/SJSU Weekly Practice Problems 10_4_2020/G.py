X = int(input())
ppls = input()
wait = ""
v = 0
np = 0
for ps in ppls:
    if ps == "M":
        v += 1
        if abs(v) > X:
            if not wait:
                wait = "M"
                v -= 1
            elif wait == "W":
                v -= 1
                np += 2
                wait = ""
            else:
                break
        else:
            np += 1
    else:
        v -= 1
        if abs(v) > X:
            if not wait:
                wait = "W"
                v += 1
            elif wait == "M":
                v += 1
                np += 2
                wait = ""
            else:
                break
        else:
            np += 1
else:
    print(np + bool(wait))
    exit()
print(np)