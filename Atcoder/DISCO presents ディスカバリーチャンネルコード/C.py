def count(n,l):
    c = 0
    for a in l:
        c += a.count(n)
    return c

H, W, K = [int(i) for i in input().split()]
cake = [list(input()) for i in range(H)]
dec = []
c = 1
for a in range(H):
    for b in range(W):
        if cake[a][b] == "#":
            dec.append([a,b])
            cake[a][b] = c
            c += 1

# for a in cake:
#     print(a)

for i,a in enumerate(dec,1):
    x,y = a
    while y > 0 and cake[x][y-1] == ".":
        cake[x][y-1] = i
        y -= 1
    y = a[1]
    while y < W - 1 and cake[x][y+1] == ".":
        cake[x][y+1] = i
        y += 1

# print()
# for a in cake:
#     print(a)

for a in range(len(cake)):
    if cake[a].count(".") == W:
        b = a
        if a != 0:
            # while cake[b].count(".") == W:
            #     b -= 1
            cake[a] = cake[a-1]
        else:
            while cake[b].count(".") == W:
                b += 1
            cake[a] = cake[b]

# print()
for a in cake:
    print(" ".join(map(str, a)))