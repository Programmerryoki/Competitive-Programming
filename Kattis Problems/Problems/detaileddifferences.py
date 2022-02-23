n = int(input())
for i in range(n):
    str1 = input()
    str2 = input()
    ans = ""
    for a in range(len(str1)):
        if str1[a] == str2[a]:
            ans += "."
        else:
            ans += "*"
    print(str1)
    print(str2)
    print(ans)
    print()