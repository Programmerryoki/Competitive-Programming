from collections import deque

H,W = [int(i) for i in input().split()]
S = [input() for i in range(H)]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

goalwall = set()
que = deque([(H-1, W-1)])
seen = {(H-1, W-1)}
while que:
    i,j = que.popleft()
    for dx,dy in moves:
        x,y = i+dx,j+dy
        if 0<=x<H and 0<=y<W and (x,y) not in seen:
            if S[x][y] == "#":
                goalwall.add((x,y))
            else:
                if (x,y) == (0,0):
                    print(0)
                    exit()
                que.append((x,y))
            seen.add((x,y))
# print(goalwall)

def getmin(x,y):
    md = float("inf")
    pos = []
    for i,j in goalwall:
        d = abs(x-i)+abs(y-j)
        if d < md:
            md = d
            pos = [(x,y),(i,j)]
    return md, pos

mind = float("inf")
que = deque([(0,0)])
seen = {(0,0)}
pos = []
while que:
    i,j = que.popleft()
    for dx,dy in moves:
        x,y = i+dx,j+dy
        if 0<=x<H and 0<=y<W and (x,y) not in seen:
            if S[x][y] == "#":
                d, p = getmin(x,y)
                if d < mind:
                    mind = d
                    pos = p
            else:
                que.append((x,y))
            seen.add((x,y))

# print(mind, pos)
(x,y),(i,j) = pos
difx = abs(x-i)
dx = -(-difx//2)
dify = abs(y-j)
dy = -(-dify//2)

print(min(dx-(-max(0,dify-dx)//2), dy-(-max(0,difx-dy)//2)))