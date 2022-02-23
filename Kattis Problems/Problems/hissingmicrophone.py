s = input()
h = False
for a in range(len(s)-1):
    if s[a]+s[a+1] == "ss":
        h = True
        break
if h:
    print("hiss")
else:
    print("no hiss")