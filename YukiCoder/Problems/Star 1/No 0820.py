n, k = [int(i) for i in input().split()]
if n >= k:
    print(2**(n-k))
else:
    print(0)