N = int(input())
graph = [[0]*10**5 for i in range(10**5)]
for _ in range(N):
    M = int(input())
    points = []
    arr = [int(i) for i in input().split()]
    for i in range(0,M,2):
        points.append(tuple(arr[i:i+2]))
    print(points)