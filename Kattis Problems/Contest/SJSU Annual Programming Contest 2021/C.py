n,k = map(int, input().split())
points = [[float(i) for i in input().split()] for i in range(n)]
x0,y0 = points[0]
area = 0
for i in range(1,k-1):
    a = [points[i][0]-x0, points[i][1]-y0]
    b = [points[i+1][0]-x0, points[i][1]-y0]
    area += abs(a[0]*b[1] - a[1]*b[0])
print(area / 2)