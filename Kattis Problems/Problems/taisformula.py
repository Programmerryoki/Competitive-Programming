N = int(input())
glucose = []
for a in range(N):
    glucose.append([float(i) for i in input().split()])
total = 0
for a in range(N-1):
    total += (glucose[a][1] + glucose[a+1][1]) / 2 * abs(glucose[a][0] - glucose[a+1][0])
print(total/1000)