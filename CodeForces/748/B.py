t = int(input())
for _ in range(t):
    n = input()[::-1]
    pos = ["00","52","05","57"]
    m = float("inf")
    for p in pos:
        i = -1
        for j in p:
            try:
                i = n.index(j, i+1)
            except:
                break
        else:
            m = min(m, i-1)
    print(m)