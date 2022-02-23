play = input()
t, c, g = 0, 0, 0
for a in play:
    if a == "T":
        t += 1
    elif a == "C":
        c += 1
    elif a == "G":
        g += 1
print(t**2 + c**2 + g**2 + min(t, c, g)*7)