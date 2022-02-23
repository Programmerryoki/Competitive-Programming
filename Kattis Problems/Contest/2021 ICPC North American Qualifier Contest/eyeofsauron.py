S = input()
b = 0
brac = False
for i in S:
    if i == "|":
        b += 1 if not brac else -1
    elif i == ")":
        brac = True
print("correct" if b == 0 else "fix")