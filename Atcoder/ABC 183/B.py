sx,sy,gx,gy = map(int, input().split())
gy = -gy
if gx == sx:
    print(gx)
    exit()

g = (sy - gy) / (sx - gx)
b = sy - (g * sx)
print((-b)/g)