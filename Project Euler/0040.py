ld = 0
d = [10**6, 10**5, 10**4, 10**3, 10**2, 10**1, 10**0]
# d = list(range(20,0,-1))
ans = 1
for n in range(1,1000000):
    ns = str(n)
    if ld + len(ns) >= d[-1]:
        ans *= int(ns[d[-1] - ld - 1])
        print(d[-1], ns[d[-1] - ld-1], ans)
        d.pop()
        if not d:
            break
    ld += len(ns)