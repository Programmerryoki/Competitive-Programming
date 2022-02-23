S = input()
search = "keyence"
for i in range(len(search)):
    if S[:i] + S[len(S) - (len(search) - i):] == search:
        print("YES")
        break
else:
    print("NO")