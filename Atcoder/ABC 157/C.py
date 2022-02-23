N, M = [int(i) for i in input().split()]
valid = True
ans = [-1]*N
for a in range(M):
    s,c = [int(i) for i in input().split()]
    if ans[s-1] == -1:
        ans[s-1] = c
    elif ans[s-1] != c:
        valid = False

for a in range(len(ans)):
    if ans[a] == -1:
        if a == 0:
            if len(ans) == 1:
                ans[a] = 0
            else:
                ans[a] = 1
        else:
            ans[a] = 0
if valid:
    n = "".join(map(str, ans))
    if len(n) != 1 and n[0] == "0":
        print(-1)
    else:
        print(int(n))
else:
    print(-1)