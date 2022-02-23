t = int(input())
for a in range(t):
    s = [int(i) for i in input().split()]
    ss = sum(s)
    ms = max(s)
    if ss - ms < ms:
        print(min(ss - ms, ms))
    else:
        print(ss//2)