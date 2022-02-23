n, h, v = [int(i) for i in input().split()]
h = max(n - h, h)
v = max(n - v, v)
print(h * v * 4)