from collections import Counter
from decimal import Decimal
from math import gcd

N = int(input())
coord = [[int(i) for i in input().split()] for j in [0]*N]
coord.sort()
cn = Counter([i[0] for i in coord])
# print(cn)
for key in cn:
    if cn[key] >= 3:
        print("Yes")
        exit()
for i in range(N-2):
    for j in range(i+1,N-1):
        if coord[i][0] == coord[j][0]:
            continue
        g = [coord[j][0] - coord[i][0], coord[j][1] - coord[i][1]]
        g = [g[0] // gcd(g[0], g[1]), g[1] // gcd(g[0], g[1])]
        for k in range(j+1, N):
            # print(i,j,k)
            g2 = [coord[k][0] - coord[j][0], coord[k][1] - coord[j][1]]
            g2 = [g2[0] // gcd(g2[0], g2[1]), g2[1] // gcd(g2[0], g2[1])]
            if g == g2:
                print("Yes")
                exit()
print("No")

# from collections import Counter
# from decimal import Decimal
#
# N = int(input())
# coord = [[int(i) for i in input().split()] for j in [0]*N]
# coord.sort()
# cn = Counter([i[0] for i in coord])
# # print(cn)
# for key in cn:
#     if cn[key] >= 3:
#         print("Yes")
#         exit()
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         if coord[i][0] == coord[j][0]:
#             continue
#         g = Decimal(coord[j][1] - coord[i][1]) / Decimal(coord[j][0] - coord[i][0])
#         d = coord[j][1] - coord[j][0]*g
#         for k in range(j+1, N):
#             # print(i,j,k)
#             y = g*coord[k][0] + d
#             if float(y).is_integer() and y == coord[k][1]:
#                 print("Yes")
#                 exit()
# print("No")