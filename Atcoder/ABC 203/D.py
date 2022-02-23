N,K = [int(i) for i in input().split()]
grid = [[int(i) for i in input().split()] for j in range(N)]
minmid = float("inf")
index = (K**2 // 2)
for i in range(N-K+1):
    # print(grid[0][i:i+K])
    for j in range(N-K+1):
        tmp = []
        for k in range(K):
            tmp.extend(grid[i+k][j:j+K])
        tmp.sort(reverse=True)
        # print(tmp)
        # print(tmp[index])
        mid = tmp[index]
        if mid < minmid:
            minmid = mid
print(minmid)