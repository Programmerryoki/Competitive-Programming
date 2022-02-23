t = int(input())
for _ in range(t):
    n = int(input())
    S = list(input())
    p = 0
    i = 0
    c = 0
    while i < len(S):
        # print(S,end = " -> ")
        if S[i] == "(":
            p += 1
            i += 1
        else:
            p -= 1
            if p < 0:
                del S[i]
                S.append(")")
                c += 1
                p = 0
            else:
                i += 1
        # print(S, i, p, c)
    print(c)