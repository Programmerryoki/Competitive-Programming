from bisect import bisect_left

T = int(input())
for _ in range(T):
    h,c,t = [int(i) for i in input().split()]
    ct = h
    pt = [[ct,1]]
    p = 1
    for _ in range(50):
        print(ct)
        p += 1
        ct = (c + ct)/2
        pt.append([ct,p])
        print(ct)
        p += 1
        ct = (h + ct)/2
        pt.append([ct,p])
    pt.sort()
    print(pt)
    n = bisect_left(pt, [t,0])
    print(n)
    print(pt[n][1])