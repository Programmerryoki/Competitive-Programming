t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ma = a.index(max(a))
    mi = a.index(min(a))
    pos = [max(ma+1, mi+1), max(n-ma, n-mi), ma+1 + n-mi, mi+1 + n-ma]
    # print(pos)
    print(min(pos))