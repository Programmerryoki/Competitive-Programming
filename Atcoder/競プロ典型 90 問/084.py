N = int(input())
S = input()
total = 0
nxt = [-1,-1]
for i in range(N-1):
    if S[i] == "o":
        if nxt[0] == -float("inf"):
            continue
        if nxt[0] < i:
            try:
                nxt[0] = S.index("x", max(nxt[0], i)+1)
            except:
                nxt[0] = -float("inf")
        if nxt[0] != -float("inf"):
            total += N - nxt[0]
    else:
        if nxt[1] == -float("inf"):
            continue
        if nxt[1] < i:
            try:
                nxt[1] = S.index("o", max(nxt[1], i)+1)
            except:
                nxt[1] = -float("inf")
        if nxt[1] != -float("inf"):
            total += N - nxt[1]
    # print(nxt)
print(total)