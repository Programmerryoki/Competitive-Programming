t = int(input())
for _ in range(t):
    x,y,a,b = [int(i) for i in input().split()]
    s = (y-x)/(a+b)
    if s.is_integer():
        print(int(s))
    else:
        print(-1)