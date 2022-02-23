s = input()
i,j,k = 0, len(s)//3, len(s)*2//3
for n in range(len(s)//3):
    if s[i+n] == s[j+n] or s[i+n] == s[k+n]:
        print(s[i+n], end="")
    else:
        print(s[j+n], end="")
print()