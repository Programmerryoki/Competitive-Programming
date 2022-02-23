N = int(input())
points = [[float(i) for i in input().split()] for j in range(N)]
A = int(input())
cross = lambda a,b: a[0]*b[1] - a[1]*b[0]
area = sum([cross(points[i], points[(i+1)%N]) for i in range(N)]) / 2
ratio = (A / area)**0.5
movex = sorted([i[0] for i in points])[0]
movey = sorted([i[1] for i in points])[0]
for i in range(N):
    points[i] = [(points[i][0] - movex)*ratio, (points[i][1] - movey)*ratio]
print("\n".join(" ".join(map(str, i)) for i in points))