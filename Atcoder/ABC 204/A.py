x,y = map(int, input().split())
if x == y:
    print(x)
else:
    print(({0,1,2}-{x,y}).pop())