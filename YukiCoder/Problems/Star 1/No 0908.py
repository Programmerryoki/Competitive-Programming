w = "abcdefghijklmnopqrstuvwxyz"
s = input()
for a in range(len(s)):
    if a%2==0:
        if s[a] not in w:
            print("No")
            break
    else:
        if s[a] != " ":
            print("No")
            break
else:
    print("Yes")