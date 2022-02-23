N,Q = [int(i) for i in input().split()]
points = [[int(i) for i in input().split()] for j in range(N)]
xm = [float("inf"), -float("inf")]
ym = [float("inf"), -float("inf")]
for i,[x,y] in enumerate(points):
    points[i][0] -= y
    points[i][1] += x
    if xm[0] > points[i][0]:
        xm[0] = points[i][0]
    if xm[1] < points[i][0]:
        xm[1] = points[i][0]
    if ym[0] > points[i][1]:
        ym[0] = points[i][1]
    if ym[1] < points[i][1]:
        ym[1] = points[i][1]

for _ in range(Q):
    q = int(input()) - 1
    x,y = points[q]
    print(max(abs(xm[0]-x), abs(xm[1]-x), abs(ym[0]-y), abs(ym[1]-y)))