t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    v,h = 0,0
    grid = []
    for _ in range(n):
        line = [int(i) for i in input().split()]
        if 1 not in line:
            h += 1
        grid.append(line)
    for i in range(m):
        if 1 not in [j[i] for j in grid]:
            v += 1
    M = min(h, v)
    if M&1:
        print("Ashish")
    else:
        print("Vivek")