from collections import deque
from sys import stdin

def main():
    input = stdin.readline
    H,W = [int(i) for i in input().split()]
    rs,cs = [int(i)-1 for i in input().split()]
    rt,ct = [int(i)-1 for i in input().split()]
    moves = [(-1,0),(0,1),(1,0),(0,-1)]

    que = deque((rs,cs,i) for i in range(4))
    S = [input() for i in range(H)]
    # dist = [[[float("inf")]*4 for i in range(W)] for j in range(H)]
    dist = {(rs, cs): [0] * 4}
    while que:
        i,j,dir = que.popleft()
        dij = dist[(i,j)]
        for d,(dx,dy) in enumerate(moves):
            x,y = i+dx, j+dy
            cost = dij[dir] + (d != dir)
            if 0 <= x < H and 0 <= y < W and S[x][y] == ".":
                tup = (x,y)
                if tup not in dist:
                    dist[tup] = [float("inf")]*4
                if dist[tup][d] <= cost:
                    continue
                dist[tup][d] = cost
                if d == dir:
                    que.appendleft((x,y,d))
                else:
                    que.append((x,y,d))
    print(min(dist[(rt,ct)]))

if __name__ == '__main__':
    main()