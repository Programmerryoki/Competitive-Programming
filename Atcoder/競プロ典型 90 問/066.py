N = int(input())
A = [[int(i) for i in input().split()] for j in range(N)]
prob = 0
for i in range(N):
    for j in range(i+1, N):
        bot = (A[i][1] - A[i][0] + 1) * (A[j][1] - A[j][0] + 1)
        up = 0
        # print(A[i], A[j], (A[i][1] - A[i][0]) * (A[j][1] - A[j][0]))
        for k1 in range(A[i][0], A[i][1]+1):
            for k2 in range(A[j][0], A[j][1]+1):
                if k1 > k2:
                    up += 1
        prob += up / bot
print(prob)