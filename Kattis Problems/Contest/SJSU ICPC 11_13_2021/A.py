N = int(input())
K = int(input())
count = {}
seen = set()
for _ in range(K):
    c1,c2,p1,p2 = input().split()
    if c1 not in seen:
        if p1 not in count:
            count[p1] = 0
        count[p1] += 1
    if c2 not in seen:
        if p2 not in count:
            count[p2] = 0
        count[p2] += 1
    seen.add(c1)
    seen.add(c2)
print(seen, count)
ans = 0
for key in count:
    ans += count[key] // 2
print(ans)