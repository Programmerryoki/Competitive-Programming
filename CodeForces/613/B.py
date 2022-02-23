from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    sl = list(accumulate(a))
    sr = list(accumulate(a[::-1]))
    tl = max(sl) - min(sl)
    tr = max(sr) - min(sr)
    # if s[0] != tm and s[-1] != tm:
    #     if
    if max(tl, tr) < sl[-1]:
        print("YES")
    else:
        print("NO")