n,m = [int(i) for i in input().split()]
if m >= n:
    print(1)
else:
    if n % 2 == 1:
        print(-1)
    elif m < n/2:
        print(-1)
    elif m != n:
        print(2)