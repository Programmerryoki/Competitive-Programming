q = int(input())
for _ in range(q):
    n,m = [int(i) for i in input().split()]
    bound = [m,m]
    ct = 0
    pos = True
    for _ in range(n):
        t,l,h = [int(i) for i in input().split()]
        td = t - ct
        ct = t
        lb, ub = bound[0] - td, bound[1] + td
        if ub < l or lb > h:
            pos = False
        bound[0],bound[1] = max(lb, l), min(ub, h)
    print("YES" if pos else "NO")