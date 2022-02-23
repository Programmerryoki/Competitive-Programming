W, H ,N = [int(i) for i in input().split()]
X = [0, W]
Y = [0, H]
for _ in range(N):
    x, y, a = [int(i) for i in input().split()]
    if a == 1:
        X = [max(X[0], x), X[1]]
        if X[0] >= X[1]:
            break
    elif a == 2:
        X = [X[0], min(X[1], x)]
        if X[0] >= X[1]:
            break
    elif a == 3:
        Y = [max(Y[0], y), Y[1]]
        if Y[0] >= Y[1]:
            break
    else:
        Y = [Y[0], min(Y[1], y)]
        if Y[0] >= Y[1]:
            break
print(max(0, X[1] - X[0]) * max(0, Y[1] - Y[0]))