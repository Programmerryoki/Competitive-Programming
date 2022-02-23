m = int(input())
for _ in range(m):
    n, T, a, b = [int(i) for i in input().split()]
    p = [a if int(i) == 0 else b for i in input().split()]
    t = [int(i) for i in input().split()]
    if sum(p) <= T:
        print(n)
    else:
        time = 0
        mand = 0
        