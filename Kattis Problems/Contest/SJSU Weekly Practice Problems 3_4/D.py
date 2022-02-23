from math import cos, radians

H, v = [int(i) for i in input().split()]
if 0 <= v <= 180:
    print("safe")
else:
    v -= 270
    print(int(H / cos(radians(abs(v)))))