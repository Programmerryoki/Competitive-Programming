t = int(input())
for _ in range(t):
    x,n = [int(i) for i in input().split()]
    if n%4 == 0:
        print(x)
    elif n%4 == 1:
        print(x+(n if x&1 else -n))
    elif n%4 == 2:
        print(x+(-1 if x&1 else 1))
    elif n%4 == 3:
        print(x+(-(n+1) if x&1 else (n+1)))