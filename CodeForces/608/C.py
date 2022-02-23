from sys import stdin
n, x, y = map(int, input().split())
       #N W S E
coor = [0,0,0,0]
for line in stdin:
    # print(line)
    sx, sy = [int(i) for i in line[:-1].split()]
    if sx == x:
        if sy < y:
            coor[0] += 1
        else:
            coor[2] += 1
    elif sy == y:
        if sx < x:
            coor[1] += 1
        elif sx > x:
            coor[3] += 1
    elif sx < x:
        if sy < y:
            coor[0] += 1
            coor[1] += 1
        else:
            coor[1] += 1
            coor[2] += 1
    elif sx > x:
        if sy < y:
            coor[0] += 1
            coor[3] += 1
        else:
            coor[3] += 1
            coor[2] += 1

mc = max(coor)
if mc == coor[0]:
    y -= 1
elif mc == coor[1]:
    x -= 1
elif mc == coor[2]:
    y += 1
else:
    x += 1
print(mc)
print(x,y)


# n, x, y = [int(i) for i in input().split()]
# s = [[int(i) for i in input().split()] for j in range(n)]
# sx = max(max([i[0] for i in s]),x)
# sy = max(max([i[1] for i in s]),y)
# # print(sx,sy)
# pos = [[0 for i in range(sx+1)] for j in range(sy+1)]
# for a in s:
#     for i in range(min(a[1],y),max(a[1],y)+1):
#         for j in range(min(a[0],x),max(a[0],x)+1):
#             pos[i][j] += 1
#
# pos[y][x] = -1
#
# # for a in pos:
# #     print(a)
#
# ans = 0
# coor = []
# for i,a in enumerate(pos):
#     ma = max(a)
#     if ma > ans:
#         ans = ma
#         coor = [a.index(ma),i]
# print(ans)
# print(coor[0],coor[1])