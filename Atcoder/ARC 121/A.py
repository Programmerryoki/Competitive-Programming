N = int(input())
houses = [[int(i) for i in input().split()] for j in range(N)]
houses.sort(key=lambda x: -(abs(x[0]) + abs(x[1])))
dis = []
ub = N//300 if N//300 > 10 else N
for i in range(ub):
    xi,yi = houses[i]
    for j in range(i+1, ub):
        xj,yj = houses[j]
        dis.append(max(abs(xi-xj), abs(yi-yj)))

dis.sort()
a1 = dis[-2]

dis = []
houses.sort(key=lambda x: -max(abs(x[0]), abs(x[1])))

for i in range(ub):
    xi,yi = houses[i]
    for j in range(i+1, ub):
        xj,yj = houses[j]
        dis.append(max(abs(xi-xj), abs(yi-yj)))

dis.sort()
print(max(dis[-2], a1))