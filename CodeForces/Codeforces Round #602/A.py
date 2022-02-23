t = int(input())
for a in range(t):
    n = int(input())
    segments =[list(map(int, input().split())) for i in range(n)]
    mi = segments[0]
    ma = segments[0]
    for b in segments:
        if mi[1] > b[1]:
            mi = b
        if ma[0] < b[0]:
            ma = b
        # print(mi, ma)
    if mi[1] >= ma[0]:
        print(0)
    else:
        print(abs(ma[0] - mi[1]))