from math import gcd

M = int(input())
for _ in range(M):
    N = int(input())
    ab = [[int(i) for i in input().split()] for j in range(N)]
    ab.sort()
    lcm = 1
    num = 0
    pos = True
    for ai,bi in ab:
        if num%ai != bi:
            p = num%ai
            s = set()
            while p != bi and not p in s:
                s.add(p)
                num += lcm
                p = num%ai
            if p != bi:
                pos = False
                break
        lcm = (lcm * ai) // gcd(lcm, ai)
    print(num if pos else "Impossible")