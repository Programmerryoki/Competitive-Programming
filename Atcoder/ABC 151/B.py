n, k, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
aim = n*m
sa = sum(a)
if aim - sa > k:
    print(-1)
else:
    print(max(aim - sa,0))