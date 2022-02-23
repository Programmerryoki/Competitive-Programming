def dis(x,y,points):
    td = 0
    for x1,y1,x2,y2 in points:
        if x < x1 or x2 < x:
            td += min(abs(x-x1),abs(x-x2))
        if y < y1 or y2 < y:
            td += min(abs(y-y1),abs(y-y2))
    return td

from sys import stdin
from math import floor

def main():
    input = stdin.readline
    T = int(input())
    for case in range(T):
        memo = {}
        K = int(input())
        points = [[int(i) for i in input().split()] for _ in range(K)]
        x = 0; y = 0; dx = 10**9 / 2
        while dx >= 10**-6:
            p = [(dx,dx),(dx,0),(0,dx),(-dx,dx),(dx,-dx),(-dx,-dx),(-dx,0),(0,-dx),(0,0)]
            pos = []
            for t in p:
                if t not in memo:
                    d = dis(x+t[0],y+t[1],points)
                    memo[t] = d
                pos.append((memo[t], t))
            pos.sort()
            x,y = x+pos[0][1][0],y+pos[0][1][1]
            dx /= 2
            print(x,y,dx)
        if round(x,2)%1 == 0.5:
            x = floor(x)
        else:
            x = round(x)
        if round(y,2)%1 == 0.5:
            y = floor(y)
        else:
            y = round(y)
        print(f"Case #{case+1}: {x} {y}")


if __name__ == '__main__':
    main()