n = int(input())
for _ in range(n):
    w,g,h,r = map(int, input().split())
    mi = ((max(g,h) - min(g,h))**2 + w**2)**0.5
    cable = lambda x: ((g-r)**2 + (w-x)**2)**0.5 + ((h-r)**2 + (x)**2)**0.5
    L,R = 0, mi
    ma = float("inf")
    for i in range(50):
        mid = (R + L) / 2
        c = cable(mid); cr = cable(mid + 0.00000001); cl = cable(mid-0.00000001)
        ma = min(c, ma)
        if cr > cl:
            R = mid
        else:
            L = mid
    print(mi, ma)