from collections import deque

moves = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]

n = int(input())
for _ in range(n):
    f,r = input()
    chess = [[-1]*8 for i in range(8)]
    pos = (int(ord(f) - ord("a")), int(r)-1)
    que = deque([pos])
    while que:
        f,r = que.popleft()
        for dx, dy in moves:
            x = dx + f
            y = dy + r
            if 0 <= x < 8 and 0 <= y < 8:
                if chess[x][y] == -1:
                    chess[x][y] = chess[f][r] + 1
                    que.append((x,y))
    m = max([max(i) for i in chess])
    ans = []
    for i in range(8):
        for j in range(8):
            if chess[i][j] == m:
                ans.append(chr(ord("a")+i) + str(j+1))
    ans.sort(key=lambda x: (-int(x[1]), x[0]))
    print(m+1," ".join(ans))