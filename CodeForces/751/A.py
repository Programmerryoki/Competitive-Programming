t = int(input())
for _ in range(t):
    s = input()
    a = sorted(set(s))[0]
    ind = s.index(a)
    b = ""
    for i in range(len(s)):
        if i != ind:
            b += s[i]
    print(a,b)