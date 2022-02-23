t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    mid = n//2
    var = [[] for i in range(n)]
