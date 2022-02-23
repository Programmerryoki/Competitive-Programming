x, y, x1, y1, x2, y2 = [int(i) for i in input().split()]

if min(y1,y2) <= y <= max(y1,y2):
    if x <= x1 and x <= x2:
        dist = min(x1, x2) - x
    else:
        dist = x - max(x1, x2)
elif min(x1, x2) <= x <= max(x1,x2):
    if y <= y1 and y <= y2:
        dist = min(y1,y2) - y
    else:
        dist = y - max(y1, y2)
else:
    checks = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
    dist = 999999999999999
    for x1, y1 in checks:
        dist = min(dist,((x-x1)**2 + (y-y1)**2)**0.5)
print(dist)