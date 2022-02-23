H,W,K = [int(i) for i in input().split()]
grid = [list(input()) for i in range(H)]
B = sum([i.count("#") for i in grid])
c = 0
for i in range(2**(H)):
    for j in range(2**(W)):
        gt = [[j for j in i] for i in grid]
        a,b = bin(i)[2:], bin(j)[2:]
        while len(a) < H:
            a = "0" + a
        while len(b) < W:
            b = "0" + b
        for x in range(H):
            if a[x] == "1":
                gt[x] = ["."]*W
        for y in range(W):
            for x in range(H):
                if b[y] == "1":
                    gt[x][y] = "."
        if sum([x.count("#") for x in gt]) == K:
            c += 1
print(c)