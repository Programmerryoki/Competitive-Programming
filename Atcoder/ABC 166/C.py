N, M = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]
graph = {i:set() for i in range(1,N+1)}
for _ in range(M):
    a,b = [int(i) for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)

c = 0
good = [-1]*N
for i in range(1,N+1):
    if good[i-1] == -1:
        h = H[i-1]
        for j in graph[i]:
            if h > H[j-1]:
                good[j-1] = 0
            else:
                good[i-1] = 0
                break
        else:
            good[i-1] = 1
            c += 1
# print(good)
print(c)