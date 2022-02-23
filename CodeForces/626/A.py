t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i, e in enumerate(a):
        if e%2==0:
            print(1)
            print(i+1)
            break
    else:
        if len(a) >= 2:
            print(2)
            print(1,2)
            continue
        else:
            print(-1)
            continue