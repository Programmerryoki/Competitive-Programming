m,n,s = map(int, input().split())
ab = [[int(i) for i in input().split()] for j in range(n)]

d = float("inf")

def bfs(rep, num):
    mm = float("inf")
    pos = True
    for a,b in ab:
        rem = (num*a + b)%m
        if rem == 0:
            global d
            d = min(len(rep), d)
        if rem in rep:
            pos = False
            continue
        temp = rep | {rem}
        M = bfs(temp, rem)
        if M != -1:
            mm = min(mm, M)
        else:
            pos = True
    if mm == float("inf"):
        return -1
    else:
        return mm
try:
    print(bfs({m}, m))
except:
    pass
print(d)