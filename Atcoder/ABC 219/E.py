from collections import deque

def main():
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    A = [[int(i) for i in input().split()] for j in range(4)]
    houses = set()
    start = None
    for i in range(4):
        for j in range(4):
            if A[i][j] == 1:
                if not start:
                    start = (i,j)
                houses.add((i,j))
    total = 0
    for n in range(2**16):
        num = bin(n)[2:][::-1]
        X = [[0]*4 for i in range(4)]
        ones = 0
        for i in range(len(num)):
            if num[i] == "0":
                continue
            ones += 1
            x,y = i//4, i%4
            X[x][y] = 1
        ok = True
        for i,j in houses:
            if X[i][j] == 0:
                ok = False
                break
        if not ok:
            continue
        que = deque([start])
        seen = {start}
        while que:
            i,j = que.popleft()
            for dx,dy in moves:
                x,y = i+dx,j+dy
                if 0<=x<4 and 0<=y<4 and X[x][y] == 1 and (x,y) not in seen:
                    que.append((x,y))
                    seen.add((x,y))
        if len(seen) != ones:
            continue
        zseen = set()
        for i in range(4):
            for j in range(4):
                if i!=0 and i!=3 and j!=0 and j!=3:
                    continue
                if X[i][j] == 1 or (i,j) in zseen:
                    continue
                que.clear()
                que.append((i,j))
                zseen.add((i,j))
                while que:
                    I,J = que.popleft()
                    for dx,dy in moves:
                        x,y = I+dx,J+dy
                        if 0<=x<4 and 0<=y<4 and X[x][y] == 0 and (x,y) not in zseen:
                            que.append((x,y))
                            zseen.add((x,y))
        if len(zseen) != 16 - ones:
            continue
        for t in houses:
            if t not in seen:
                break
        else:
            # for i in X:
            #     print(i)
            # print()
            total += 1
    print(total)


if __name__ == '__main__':
    main()