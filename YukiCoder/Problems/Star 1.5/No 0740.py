from math import ceil
N,M,P,Q = [int(i) for i in input().split()]
m = 1
t = 0
while N > 0:
    if P <= m < P+Q:
        N -= M*2
    else:
        N -= M
    m += 1
    if m > 12:
        m = 1
    t += 1
print(t)