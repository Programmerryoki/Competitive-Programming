S = input()
S = set(S)
for i in range(26):
    w = chr(ord("a") + i)
    if not w in S:
        print(w)
        break
else:
    print("None")