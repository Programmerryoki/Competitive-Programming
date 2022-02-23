from bisect import bisect_right

N,M,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
for i in range(len(A)):
    A[i] = [A[i], i]
A.sort(reverse=True)

best = float("inf")
PW = []
indexes = []
for i,a in enumerate(A):
    dif = K - a[0]
    all = []
    for j,[v, tmp] in enumerate(A[i:], i):
        if v == 0:
            continue
        t = dif // v
        d = v * (t+1) - dif
        PW += [(a[1], tmp)] * t
        all.append((dif, v, j, len(PW)))
        dif -= v * t
    md = float("inf")
    ind = -1
    stop = -1
    for i in all:
        for j in all:
            if (j[1] - i[0]) > 0 and (j[1] - i[0]) < md:
                md = j[1] - i[0]
                ind = j[2]
                stop = i[3]
    PW = PW[:stop] + [(a[1], A[ind][1])]
    indexes.append(len(PW))

stopping = bisect_right(indexes, 1000)
print("\n".join(" ".join(str(i) for i in j) for j in PW[:indexes[stopping-1]]))