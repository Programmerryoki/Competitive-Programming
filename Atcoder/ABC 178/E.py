N = int(input())
points = [[int(i) for i in input().split()] for j in range(N)]
points.sort(key = lambda x : x[0])
