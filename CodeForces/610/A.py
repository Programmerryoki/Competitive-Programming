t = int(input())
for _ in range(t):
    a,b,c,r = [int(i) for i in input().split()]
    a, b = min(a,b), max(a,b)
    t = b - a
    if c < a:
        t -= max(0, min(c+r-a, b-a))
    elif b < c:
        t -= max(0, min(b-(c-r), b-a))
    else:
        t -= max(0, min(b-c, r))
        t -= max(0, min(c-a, r))
    print(t)