from collections import Counter
import math

t = int(input())
for _ in range(t):
    n = int(input())
    c = [int(i) for i in input().split()]
    cn = list(Counter(c).values())
    # print(cn)
    s = min(cn)
    if max(cn) - 1 == s:
        print(len(cn))  # actual output
    else:
        cnmod = [i%s for i in cn]
        # print(cnmod)
        cndiv = [math.ceil(i/s) for i in cn]
        if cnmod.count(s-1) + cnmod.count(0) == len(cnmod):
            print(sum(cndiv))  # actual output
        else:
            cndiv2 = [math.ceil(i/(s+1)) for i in cn]
            # print(cndiv, cndiv2)
            print(min(sum(cndiv), sum(cndiv2)))