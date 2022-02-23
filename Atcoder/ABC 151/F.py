N = int(input())
coor = []
for _ in range(N):
    coor.append([int(i) for i in input().split()])

m = 0
for c1 in coor:
    for c2 in coor:
        d = ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)**0.5
        if d > m:
            m = d
print(m/2)



# N = int(input())
# x = 0
# y = 0
# coor = []
# for a in range(N):
#     c = [int(i) for i in input().split()]
#     x += c[0]
#     y += c[1]
#     coor.append(c)
#
# x /= N
# y /= N
# # print(x,y)
# m = 0
# for a,b in coor:
#     dis = ((x-a)**2 + (y-b)**2)**0.5
#     # print(a,b,dis)
#     if dis > m:
#         m = dis
# print(m)