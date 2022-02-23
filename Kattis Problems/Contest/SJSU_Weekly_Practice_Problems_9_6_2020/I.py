m = int(input())
tr = []
tc = []
for _ in range(m):
    obj, *cord = input().split()
    if obj == "rectangle":
        tr.append([int(i) for i in cord])
    else:
        tc.append([int(i) for i in cord])

ans = []
n = int(input())
for _ in range(n):
    x,y = [int(i) for i in input().split()]
    th = 0
    for x1,y1,x2,y2 in tr:
        if not (x < x1 or x2 < x or y < y1 or y2 < y):
            th += 1
    for x1, y1, r in tc:
        if ((x1-x)**2 + (y1-y)**2)**0.5 <= r:
            th += 1
    ans.append(th)
print("\n".join(map(str, ans)))