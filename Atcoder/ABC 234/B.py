N = int(input())
points = [[int(i) for i in input().split()] for _ in range(N)]
md = 0
dis = lambda a,b: (a[0]-b[0])**2 + (a[1]-b[1])**2
for i in range(len(points)):
    for j in range(len(points)):
        if i == j:
            continue
        md = max(md, dis(points[i], points[j]))
print((md)**0.5)