while True:
    n = int(input())
    if n == 0:
        break
    graph = {}
    npwc = 0

    for _ in range(n):
        v, m, d, *child = [int(i) for i in input().split()]
        graph[v] = set(child)
        npwc += m != 0

