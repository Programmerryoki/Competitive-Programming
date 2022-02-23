s = input()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print(i+1,i+2)
        exit()
    elif i != len(s)-2 and s[i] == s[i+2]:
        print(i+1,i+3)
        exit()
print(-1,-1)