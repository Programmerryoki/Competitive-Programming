N,M = map(int, input().split())
student = [input() for i in range(N)]
total = 0
for i in range(N-1):
    for j in range(i+1, N):
        dif = sum([1 for k in range(M) if student[i][k] != student[j][k]])
        if dif&1:
            total += 1
print(total)