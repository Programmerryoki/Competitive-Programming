D = input()
E = input()
I = int(input())
stuff = [input() for i in range(I)]
TD = input()

used = set()
order = []
pos = []
def dfs(word, target):
    if word == target:
        pos.append(list(order))
        return
    if len(used) == I:
        return
    for i in range(I):
        if i in used:
            continue
        order.append(i)
        used.add(i)
        dfs(chr(stuff[i].index(word) + ord("a")), target)
        used.remove(i)
        order.pop()

dfs(E[0], D[0])
for order in pos:
    for i in range(1,len(E)):
        s = D[i]
        if s == " ":
            continue
        for j in range(len(order)-1,-1,-1):
            s = stuff[order[j]][ord(s)-ord("a")]
        if s != E[i]:
            break
    else:
        ans = ""
        for w in TD:
            if w == " ":
                ans += w
                continue
            for j in range(len(order)):
                w = chr(stuff[order[j]].index(w) + ord("a"))
            ans += w
        print(ans)
        break