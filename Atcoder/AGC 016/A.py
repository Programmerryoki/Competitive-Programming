s = input()
best = float("inf")
for j in range(26):
    w = chr(ord("a")+j)
    t = s
    moves = 0
    while len(set(t)) != 1:
        ns = ""
        for i in range(len(t)-1):
            if t[i] == w or t[i+1] == w:
                ns += w
            else:
                ns += t[i]
        t = ns
        moves += 1
    if moves < best:
        best = moves
print(best)