N = int(input())
c = []
m = 0
for _ in range(N):
    line = [int(i) for i in input().split()]
    c.append(line[1:])
    m = max(line[0], m)
ans = []
for i in range(m):
    for j in range(N):
        try:
            ans.append(c[j][i])
        except:
            continue
print(" ".join(map(str, ans)))