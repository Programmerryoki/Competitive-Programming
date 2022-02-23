from bisect import bisect_left, bisect_right

N = int(input())
A = [int(i) for i in input().split()]
forward = []
lf = []
for i in A:
    ind = bisect_left(forward, i)
    if ind == len(forward):
        forward.append(i)
    else:
        forward[ind] = i
    lf.append(ind+1)
# print(forward)
# print(lf)
backward = []
lb = []
for i in A[::-1]:
    ind = bisect_left(backward, i)
    if ind == len(backward):
        backward.append(i)
    else:
        backward[ind] = i
    lb.append(ind+1)
lb = lb[::-1]
# print(backward)
# print(lb)
m = 0
for i in range(N):
    if m < lf[i] + lb[i] - 1:
        m = lf[i] + lb[i] - 1
print(m)