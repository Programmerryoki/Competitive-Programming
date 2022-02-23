from bisect import bisect_left

N = int(input())
A = [[int(v),i] for i,v in enumerate(input().split())]
B = [[int(v),i] for i,v in enumerate(input().split())]
B.sort()
indB = {}
Bind = {}
for v,i in B:
    indB[i] = v

total = 0
for v, i in A:
    ind = bisect_left(B, [indB[i], -1])
    total += indr - indl - (indB[i]==v)
print(total)