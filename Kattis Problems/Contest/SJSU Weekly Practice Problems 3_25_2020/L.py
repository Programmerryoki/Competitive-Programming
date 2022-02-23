import bisect

N, K = [int(i) for i in input().split()]
vline = [[] for i in range(N)]
md = 0
for _ in range(K):
    p, d = [int(i) for i in input().split()]
    if md < d:
        md = d
    vline[p].append([d, p+1])
    vline[p+1].append([d, p])

for i in range(N):
    vline[i].sort()
# print(vline)

ans = [-1]*N
for vn in range(N):
    if len(vline[vn]) == 0:
        ans[vn] = vn
        continue
    pos = vn
    d = 0
    prev = vn
    # print(ans)
    while True:
        index = bisect.bisect_left(vline[pos], [d, -1])
        if index == len(vline[pos]):
            break

        # print(pos, d, index, prev)
        while [d, prev] == vline[pos][index]:
            index += 1
            if index > len(vline[pos]) - 1:
                break
        else:
            prev = pos
            d, pos = vline[pos][index]
            continue
        break
    ans[vn] = pos
print(" ".join(map(str, ans)))