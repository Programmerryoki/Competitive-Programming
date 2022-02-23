from math import pi

M,N,R = map(float, input().split())
ax,ay,bx,by = map(int, input().split())
r = R / N
ri = min(ay,by)*r
ro = abs(ay-by)*r
# arc = 2 * pi * ri * ((180 / M) / 360)
diss = [r*(ay-i) + r*(by-i) + pi*r*i*(1/M)*abs(ax-bx) for i in range(min(int(N),ay+1,by+1))]
# print(diss)
print(min(diss))
# print(min(ro + abs(ax-bx)*arc, r * (ax + bx)))