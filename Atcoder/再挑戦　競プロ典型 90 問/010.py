from bisect import bisect_left, bisect_right

N = int(input())
clas = [[],[]]
points = [[0],[0]]
for ind in range(1,N+1):
    C,P = [int(i) for i in input().split()]
    clas[C-1].append(ind)
    points[C-1].append(P)
for c in range(2):
    for i in range(1,len(points[c])):
        points[c][i] += points[c][i-1]

ans = []
Q = int(input())
for i in range(Q):
    L,R = [int(i) for i in input().split()]
    t = []
    for c in range(2):
        indl = bisect_left(clas[c], L)
        indr = bisect_right(clas[c], R)
        t.append(points[c][indr] - points[c][indl])
    ans.append(t)
print("\n".join(" ".join(str(i) for i in j) for j in ans))