T = int(input())
for _ in range(T):
    n = int(input())
    p = [[0,0] for i in range(n)]
    for i in range(n):
        s = input()
        for j in s:
            if j == "1":
                p[i][0] += 1
            elif j == "d":
                p[i][0] += 0.5
            elif j == ".":
                p[i][1] += 1
    m = max([i[0] for i in p])
    pos = []
    for i,a in enumerate(p,1):
        if sum(a) >= m:
            pos.append(i)
    print(p)
    print(" ".join(map(str, pos)))