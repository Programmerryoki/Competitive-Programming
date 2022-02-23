t = int(input())
for _ in range(t):
    x,y,n = [int(i) for i in input().split()]
    print((n//x) * x + y if (n//x) * x + y <= n else (n//x - 1) * x + y)