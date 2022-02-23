t = int(input())
for a in range(t):
    s, c = input().split()
    s,c = list(s), list(c)
    pos = True
    i = 0
    while i < min(len(c),len(s)):
        # print(s,c)
        if ord(s[i]) < ord(c[i]) or (s[i] == "A" and c[i] == "A"):
            i += 1
            # print("increment i to",i)
        else:
            j = i
            while j < len(s) and ord(s[j]) > ord(c[i]):
                # print(s[j],c[i])
                j += 1

            if j < len(s):
                s[i], s[j] = s[j], s[i]
                break
            else:
                i += 1
    # print(s,c)
    if "".join(s) < "".join(c):
        pos = True
    else:
        pos = False
    if pos:
        print("".join(s))
    else:
        print("---")