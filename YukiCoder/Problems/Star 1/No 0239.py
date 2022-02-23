N = int(input())
A = [input().split() for i in range(N)]
lst = list(zip(*A))
ny = []
for i in range(N):
    if lst[i].count("nyanpass") == N-1:
        ny += [i+1]
if len(ny) == 1:
    print(ny[0])
else:
    print(-1)