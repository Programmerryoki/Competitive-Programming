N = int(input())
ra = []
for i in range(N):
    t,l,r = [int(i) for i in input().split()]
    if t == 1:
        ra.append((l,r))
    elif t == 2:
        ra.append((l,r-0.1))
    elif t == 3:
        ra.append((l+0.1, r))
    else:
        ra.append((l+0.1, r-0.1))
count = 0
for i in range(N-1):
    l,r = ra[i]
    for j in range(i+1, N):
        L,R = ra[j]
        # print(l,r,L,R)
        if r < L or R < l:
            continue
        count += 1
print(count)