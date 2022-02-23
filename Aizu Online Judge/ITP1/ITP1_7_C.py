r, c = [int(i) for i in input().split()]
ss = []
for _ in range(r):
    s = [int(i) for i in input().split()]
    ss.append(s + [sum(s)])

ans = [[i[j] for i in ss] for j in range(c+1)]
ss.append([sum(i) for i in ans])
print("\n".join(" ".join(map(str, i)) for i in ss))