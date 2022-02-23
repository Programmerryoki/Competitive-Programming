N = int(input())
calc = [[] for i in range(N)]
ma = -1000000
mi = 1000000
for i in range(N):
    x,v = map(int, input().split())
    calc[i] = [x,v]
    ma = max(ma, x); mi = min(mi, x)
# print(ma, mi)
l = 0; r = 10**9
for _ in range(100):
    # print(l,r)
    mid = (r + l) / 2
    p = [float("inf"),-float("inf")]
    emi = []; ema = []
    for x,v in calc:
        n = x + v * mid
        if p[0] > n:
            p[0] = n
            emi = [x,v]
        if p[1] < n:
            p[1] = n
            ema = [x,v]
    # print(emi, ema)
    # print(p)
    if ma - mi > p[1] - p[0]:
        ma, mi = p
    if ema[1] - emi[1] < 0:
        l = mid
    elif ema[1] - emi[1] > 0:
        r = mid
    else:
        break
    if l >= r:
        break
print(p[1] - p[0])