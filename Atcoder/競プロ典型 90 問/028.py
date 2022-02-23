N = int(input())
grid = [[0]*1001 for i in range(1001)]
for _ in range(N):
    lx,ly,rx,ry = [int(i) for i in input().split()]
    grid[lx][ly] += 1
    if ry <= 1000:
        grid[lx][ry] -= 1
    if rx <= 1000:
        grid[rx][ly] -= 1
    if ry <= 1000 and rx <= 1000:
        grid[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        grid[i][j] += grid[i][j-1]
for i in range(1, 1001):
    for j in range(1001):
        grid[i][j] += grid[i-1][j]

count = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        count[grid[i][j]] += 1
# print(count)
print("\n".join(str(count[i]) for i in range(1,N+1)))