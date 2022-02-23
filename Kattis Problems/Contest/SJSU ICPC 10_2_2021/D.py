N = int(input())
coord = [[float(i) for i in input().split()] for _ in range(N)]
mid = float("inf")
for i in range(N):
    x1,y1 = coord[i]
    x2,y2 = coord[(i+1)%N]
    mad = 0
    for j in range(N):
        I,J = coord[j]
        if x1 == x2:
            mad = max(mad, I-x1)
        else:
            a = (y2-y1)/(x2-x1)
            b = y1 - a * x1
            x = (a * J + I - a * b) / (a**2 + 1)
            y = a * x + b
            d = ((x-I)**2 + (y-J)**2)**0.5
            mad = max(mad, d)
    if mad:
        mid = min(mid, mad)
print(mid)