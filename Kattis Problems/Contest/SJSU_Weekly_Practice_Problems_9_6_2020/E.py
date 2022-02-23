while True:
    n = int(input())
    if n == -1:
        break
    graph = [[int(i) for i in input().split()] for j in range(n)]
    wv = []
    for i in range(n):
        weak = True
        for j in range(n):
            if graph[i][j] == 1:
                for k in range(n):
                    if graph[j][k] == 1:
                        if graph[k][i] == 1:
                            weak = False
                            break
        if weak:
            wv.append(i)
    print(" ".join(map(str, wv)))