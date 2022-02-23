from math import ceil

cloud = 1
while True:
    W,N = map(int, input().split())
    if W == 0 and N == 0:
        break
    words = []
    for _ in range(N):
        S,C = input().split(); C = int(C)
        words.append([S,C])
    cmax = max([i[1] for i in words])
    h = 0
    w = 0
    rm = 0
    for S,C in words:
        P = 8 + ceil((40 * (C - 4)) / (cmax - 4))
        width = ceil((9 * len(S) * P) / 16)
        # print(S,C,P,width,w,rm)
        if w == 0:
            w = width
            rm = P
        elif w + width + 10 > W:
            h += rm
            rm = P
            w = width
        else:
            if w != 0:
                w += 10
            w += width
            rm = max(rm, P)
    h += rm
    print("CLOUD "+str(cloud)+":",h)
    cloud += 1