t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    X = [n-int(i) for i in input().split()]
    X.sort()
    for i,v in enumerate(X):
        if v < n:
            n -= v
        else:
            break
    else:
        print(k)
        continue
    print(i)