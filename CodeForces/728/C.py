t = int(input())
for _ in range(t):
    n = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    dif = [d[i]-d[i-1] for i in range(1,n)]
    s = sum(dif)
    for i in range(1,len(dif)):
        for j in range(len(dif)-i):
            dif[j] = dif[j] + dif[j+1]
        # print(dif)
        dif.pop()
        s += sum(dif)
    # print(dif)
    # print(s)
    print(d[-1] - s)