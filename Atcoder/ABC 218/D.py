from bisect import bisect_right

N = int(input())
points = [tuple(int(i) for i in input().split()) for j in range(N)]
sp = set(points)

samex = {}
samey = {}
for x,y in points:
    if x not in samex:
        samex[x] = []
    samex[x].append((x,y))
    if y not in samey:
        samey[y] = []
    samey[y].append((x,y))
for x in samex:
    samex[x].sort()
for y in samey:
    samey[y].sort()

# print(samex)
# print(samey)
# print(sp)
count = 0
for x in sorted(samex):
    for i,a in enumerate(samex[x]):
        for b in samex[x][i+1:]:
            # print(a,b)
            y = a[1]
            for c in samey[y]:
                # print("\t",c, (c[0],b[1]),b[1] > y and (c[0],b[1]) in sp)
                if c[0] > a[0] and (c[0],b[1]) in sp:
                    count += 1
print(count)