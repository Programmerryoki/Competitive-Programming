N = int(input())
x,y = [int(i) for i in input().split()]
n = max(-1, y-x)
for _ in range(N-1):
    x,y = [int(i) for i in input().split()]
    if max(-1, y-x) != n:
        print(-1)
        break
else:
    if n != 0:
        print(n)
    else:
        print(-1)