from sys import stdin

input = stdin.readline

N,H = map(int, input().split())
hei = [[0,0] for i in range(H)]
for i in range(N):
    h = int(input())
    if i&1:
        h = H - h
        hei[h][1] += 1
    else:
        hei[0][1] += 1
        hei[h][0] += 1
    # print(h, hei)

# print(hei)

n = 0
minn = float("inf")
total = 0
for i in range(H):
    n += hei[i][1]
    n -= hei[i][0]
    if n < minn:
        total = 1
        minn = n
    elif n == minn:
        total += 1
    # print(n, minn, total)
print(minn, total)