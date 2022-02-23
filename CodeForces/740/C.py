import random

t = int(input())
for _ in range(t):
    n = int(input())
    inputs = []
    for i in range(n):
        k = random.randint(1, 1000)
        tmp = [random.randint(1,1000) for j in range(k)]
        inputs.append(tmp)

    ms = []
    for i in range(n):
        # k,*rest = [int(j) for j in input().split()]
        k,*rest = [int(j) for j in inputs[i]]
        m = 0
        mind = -1
        for ind,v in enumerate(rest):
            if v > m:
                m = v
                mind = ind
        ms.append((m, mind, k))
    ms.sort(key=lambda x: -((x[0]-x[1])/x[2]))
    # print(ms)
    power = 0
    increase = 0
    for m,mind,k in ms:
        if power+increase+mind <= m:
            power += m - (power+increase+mind) + 1
        increase += k
    print(power)

    from itertools import permutations
    mp = float("inf")
    for per in permutations(ms, len(ms)):
        power = 0
        increase = 0
        for m,mind,k in ms:
            if power+increase+mind <= m:
                power += m - (power+increase+mind) + 1
            increase += k
        mp = min(mp, power)
    print(mp)