N = int(input())
x = [int(i) for i in input().split()]
if len(set(x)) == len(x):
    x.sort()
    xd = {}
    for i in range(1,N):
        d = x[i] - x[i-1]
        try:
            xd[d] += 1
        except:
            xd[d] = 1
    print("YES" if len(xd.keys()) == 1 else "NO")
else:
    print("NO")