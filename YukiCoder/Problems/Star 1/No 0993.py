s = input()
for i in range(len(s)-1):
    if s[i:i+2] == "ao":
        s = s[:i] + "ki" + s[i+2:]
print(s)