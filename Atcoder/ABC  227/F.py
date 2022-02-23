H,W,K = [int(i) for i in input().split()]
# A = [[int(i) for i in input().split()] for _ in range(H)]
test = [[0]*(W) for i in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 or j == 0:
            test[i][j] = 1
        else:
            test[i][j] = max(test[i][j], test[i-1][j]+test[i][j-1])
for i in test:
    print(i)