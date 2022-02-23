N = int(input())
pos = [[int(i) for i in input().split()] for j in range(N)]
X,Y = [list(i) for i in zip(*pos)]
X.sort()
Y.sort()
mx = (X[N//2] + X[(N-1)//2]) / 2
my = (Y[N//2] + Y[(N-1)//2]) / 2
total = 0
for i,j in pos:
    total += abs(mx - i) + abs(my - j)
print(round(total))