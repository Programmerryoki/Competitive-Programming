t = int(input())
for _ in range(t):
    s = input()
    ss = set(s)
    mv = int(min(set("012") - ss))
    cv = 0
    pv = ""
    s += " "
    for i in range(len(s)):
        if s[i] == pv:
            continue
        cv += (pv == "0")
        pv = s[i]
    print(min(mv, cv))