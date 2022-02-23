s = list(input())
for i in range(len(s)):
    if ord(s[i]) - ord("a") < 0:
        s[i] = s[i].lower()
    else:
        s[i] = s[i].upper()
print("".join(s))