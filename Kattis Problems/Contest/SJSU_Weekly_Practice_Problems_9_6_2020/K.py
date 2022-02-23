K = int(input())
graph = [-1]*100
while True:
    line = [int(i) for i in input().split()]
    if len(line) == 1 and line[0] == -1:
        break
    a,*b = line
    for i in b:
        graph[i-1] = a

path = []
while K != -1:
    path.append(K)
    K = graph[K-1]
print(" ".join(map(str, path)))