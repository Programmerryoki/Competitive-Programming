from collections import deque

moves = [[0,1],[0,-1],[1,0],[-1,0]]

r,c = map(int, input().split())
maps = [input() for i in range(r)]
map = [[-1]*c for i in range(r)]
n = int(input())
for case in range(n):
    rs,cs,re,ce = [int(i)-1 for i in input().split()]
    if maps[rs][cs] != maps[re][ce] or (map[rs][cs] != -1 and map[re][ce] != -1 and map[rs][cs] != map[re][ce]):
        print("neither")
        continue
    if map[rs][cs] != -1 and map[re][ce] != -1 and map[rs][cs] == map[re][ce]:
        print("decimal" if int(maps[rs][cs]) else "binary")
        continue
    sim = maps[rs][cs]
    que = deque([(rs,cs)])
    while que:
        ri,ci = que.popleft()
        for dx,dy in moves:
            x = dx + ri
            y = dy + ci
            if 0 <= x < r and 0 <= y < c:
                if map[x][y] == -1 and maps[x][y] == sim:
                    map[x][y] = case
                    que.append((x,y))
    if map[rs][cs] == map[re][ce]:
        print("decimal" if int(maps[rs][cs]) else "binary")
    else:
        print("neither")
# for i in map:
#     print(i)