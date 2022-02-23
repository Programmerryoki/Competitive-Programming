while True:
    n,m = map(int, input().split())
    if n == m == 0:
        break

    dh = [int(input()) for i in range(n)]
    kh = [int(input()) for i in range(m)]
    if len(dh) > len(kh):
        print("Loowater is doomed!")
        continue
    dh.sort()
    kh.sort()
    k = 0
    mon = 0
    for d in dh:
        if k >= len(kh):
            print("Loowater is doomed!")
            break
        while k < len(kh) and d > kh[k]:
            k += 1
        if k < len(kh):
            mon += kh[k]
            k += 1
    else:
        print(mon)