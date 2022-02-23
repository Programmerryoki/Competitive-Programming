import re

while True:
    N = int(input())
    if N == 0:
        break
    mw = ""
    mn = 0
    for a in range(N):
        s = input()
        count = 0
        c = 0
        while c < len(s) - 1:
            if s[c] in "aeiou":
                if s[c] == s[c+1]:
                    count += 1
                    c += 1
            c += 1
        if count > mn:
            mw = s
    print(mw)