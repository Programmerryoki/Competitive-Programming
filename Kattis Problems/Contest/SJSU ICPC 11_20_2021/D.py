from heapq import heappop, heappush

n,t = [int(i) for i in input().split()]
tech = [(-1,0,0) for i in range(t)]
que = []
pt = 0
time = [[0,0],[0,0]]
for i in range(n+1):
    if i < n:
        d, p, k = input().split(); d = int(d); k = int(k); p = int(p!="S")
        heappush(que, (p, d, k))
        if pt == d:
            continue
        print(que)
        pt = d
    else:
        pt = float("inf")
        print(tech)
        print(time)
    for i in range(t):
        if tech[i][0] + tech[i][1] <= pt:
            d,p,k = tech[i]
            time[p][0] += k - d
            time[p][1] += 1
            tech[i] = (-1,0,0)
        if tech[i][0] == -1 and que:
            p,d,k = heappop(que)
            tech[i] = (d, p, pt+k)
print(time)