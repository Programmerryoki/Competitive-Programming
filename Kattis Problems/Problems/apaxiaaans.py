s = list(input())
a = 0
while a < len(s)-1:
    if s[a] == s[a+1]:
        del s[a+1]
    else:
        a += 1
print("".join(s))