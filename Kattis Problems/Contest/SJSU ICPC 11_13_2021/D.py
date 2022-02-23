from math import pi

M,N,R = [float(i) for i in input().split()]
M = int(M); N = int(N)
ax,ay,bx,by = map(int, input().split())
unit = R / N
mind = float("inf")
# print(unit)
for i in range(min(ay,by)+1):
    d = unit * (abs(ay-by) + 2*(min(ay,by) - i)) + (abs(ax-bx)*pi*i*unit/M)
    # print(abs(ay-by) + 2*(min(ay,by) - i))
    # print(i, d)
    mind = min(mind, d)
print(mind)