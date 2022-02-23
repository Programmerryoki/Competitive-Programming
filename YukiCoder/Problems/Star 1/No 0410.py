px,py = [int(i) for i in input().split()]
qx, qy = [int(i) for i in input().split()]
print((abs(px-qx) + abs(py - qy)) / 2)