H, W, K, V = [int(i) for i in input().split()]
area = [[int(i)+K for i in input().split()] for j in range(H)]
cost = [[[0 for a in range(W-i)] for i in range(W)] for j in range(H)]

ma = 0
for l in range(W):
    for h in range(H):
        for w in range(W):
            # print(h,w,l)
            if w < W - l:
                cost[h][w][l] = sum(area[h][w:w+l+1])

# for h in range(H):
#     for w in range(W):
#         print(cost[h][w], end = " , ")
#     print()

mincost = [[0 for j in range(W)] for i in range(H)]
for h in range(H):
    for w in range(h,W):
        lst = cost[h][w]
        i = 0
        while i < len(lst) and lst[i] <= V:
            i += 1
        if i != 0:
            mincost[h][w] = i

ma = 0
for h in range(H):
    ma = max(ma, max(mincost[h]))
print(ma)