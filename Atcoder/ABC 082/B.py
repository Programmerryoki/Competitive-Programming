s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
for i in range(min(len(s), len(t))):
    if ord(s[i]) < ord(t[i]):
        print("Yes")
        exit()
    elif ord(s[i]) > ord(t[i]):
        print("No")
        exit()
print("Yes" if len(s) < len(t) else "No")