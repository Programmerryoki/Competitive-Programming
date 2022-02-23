from math import log2

N = int(input())

for _ in range(N):
    n, x, y, w, h = [int(i) for i in input().split()]
    ans = [[0]*w for i in range(h)]
    for row in range(h):
        if log2(row + y).is_integer():
            for col in range(w):
                if (row + y) == 0:
                    ans[row][col] = 1
                elif (col + x)//(row + y)%2 == 0:
                    ans[row][col] = 1
                else:
                    ans[row][col] = 0
        else:
            if (row + y)%4 == 0:
                for col in range(w):
                    if (col + x)%4 == 0