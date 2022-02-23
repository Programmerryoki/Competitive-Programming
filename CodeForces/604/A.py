ws = set("abc")
t = int(input())
for _ in range(t):
    s = list(input())
    w = ""
    valid = True
    for a in range(len(s)):
        if w == s[a]:
            valid = False
            break
        if s[a] == "?":
            if a < len(s) - 1:
                w += s[a+1]
            temp = ws - set(w)
            if len(temp) == 1:
                s[a] = temp.pop()
            else:
                s[a] = temp.pop()
        w = s[a]
    if valid:
        print("".join(s))
    else:
        print(-1)