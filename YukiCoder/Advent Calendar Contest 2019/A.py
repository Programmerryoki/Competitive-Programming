n = int(input())
ans = []
bad = []
for a in range(n):
    cheat, p = input().split()
    if p not in ans and p not in bad:
        ans.append(p)
    if cheat in ans:
        ans.remove(cheat)
    else:
        bad.append(cheat)
for a in ans:
    print(a)