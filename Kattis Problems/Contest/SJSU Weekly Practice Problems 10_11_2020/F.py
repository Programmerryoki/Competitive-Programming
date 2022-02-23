N,H,W = map(int, input().split())
disp = [[1]*W for i in range(H)]
un = {i:0 for i in range(1,30000)}
un[1] = H*W
m = 2

for _ in range(N):
    inp = [input() for i in range(H)]
    seen = {}
    for i in range(H):
        for j in range(W):
            if inp[i][j] == "*":
                seen.setdefault(disp[i][j], set())
                seen[disp[i][j]].add(str(i)+" "+str(j))
    for key in seen:
        if len(seen[key]) == un[key]:
            continue
        for l in seen[key]:
            i,j = [int(i) for i in l.split()]
            disp[i][j] = m
        un[key] -= len(seen[key])
        un[m] += len(seen[key])
        m += 1

    # print(seen)
    m += 1

# for i in disp:
#     print(i)
ans = set()
for i in disp:
    ans.update(set(i))
print(len(ans))

# from collections import deque
# N,H,W = map(int, input().split())
# disp = [[1]*W for i in range(H)]
# dn = [0]*(H*W); dn[0] = H*W
# m = 1
# move = [[0,1],[1,0],[-1,0],[0,-1]]
#
# def bfs(i,j,inp,seen,ori):
#     que = deque([[i,j]])
#     while que:
#         i,j = que.popleft()
#         for dx, dy in move:
#             x = dx + i; y = dy + j
#             string = str(x) + " " + str(y)
#             if 0 <= x < H and 0 <= y < W and not string in seen and inp[x][y] == "*":
#                 que.append([x,y])
#                 seen.add(string)
#                 if disp[x][y] != ori:
#
#
#
#
# for _ in range(N):
#     inp = [input() for i in range(H)]
#     seen = set()
#     for i in range(H):
#         for j in range(W):
#             string = str(i) + " " + str(j)
#             if not string in seen and inp[i][j] == "*":
#                 ori = disp[i][j]
#                 bfs(i,j,inp,seen,ori)
#
# print(m)