x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
z = [int(i) for i in input().split()]
area = lambda a, b, c : abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2
ar = area(x,y,z)
print(round(ar, 1))

trees = int(input())
count = 0
for _ in range(trees):
    t = [int(i) for i in input().split()]
    sums = area(x,y,t) + area(x,t,z) + area(t,y,z)
    if sums == ar:
        count += 1
print(count)


# from math import asin, acos, degrees
# coor = [[int(i) for i in input().split()] for j in range(3)]
# coor.sort()
# xa, ya = coor[0]
# xb, yb = coor[1]
# xc, yc = coor[2]
# area = round(abs(xa*(yb-yc) + xb*(yc-ya) + xc*(ya-yb)) / 2, 1)
# print(area)
# v1 = [xa - xb, ya - yb]
# v1r = [-v1[0], -v1[1]]
# v2 = [xc - xb, yc - yb]
#
# absxy = lambda x,y : (x[0]**2 + x[1]**2)**0.5 * (y[0]**2 + y[1]**2)**0.5
# xcy = lambda x,y : x[0]*y[1] - x[1]*y[0]
# cangle = lambda x,y : asin(xcy(x, y) / absxy(x, y))
#
# # print(v1r)
# # print(asin(xcy(v1, v2) / absxy(v1, v2)))
# angle = degrees(cangle(v1, v2))
# angler = degrees(cangle(v1r, v2))
# print(angle)
# print()
# coords = []
# n = int(input())
# count = 0
# for _ in range(n):
#     tree = [int(i) for i in input().split()]
#     print(tree)
#     temp = [tree[0] - xb, tree[1] - yb]
#     try:
#         ang = degrees(cangle(v1, temp))
#         if 0 <= angle:
#             if 0 <= ang <= 180:
#                 coords.append(tree)
#         else:
#             if -180 <= ang <= 0:
#                 coords.append(tree)
#     except:
#         coords.append(tree)
#         continue
# print(coords)
# ans = []
# for tree in coords:
#     print(tree)
#     temp = [tree[0] - xb, tree[1] - yb]
#     try:
#         ang = degrees(cangle(v1r, temp))
#         if 0 <= angler:
#             if 0 <= ang <= 180:
#                 count += 1
#                 ans.append(tree)
#         else:
#             if -180 <= ang <= 0:
#                 count += 1
#                 ans.append(tree)
#     except:
#         count += 1
#         ans.append(tree)
#         continue
# print(count)
# print(ans)