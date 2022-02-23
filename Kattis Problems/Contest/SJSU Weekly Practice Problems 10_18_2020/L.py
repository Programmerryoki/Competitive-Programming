N = int(input())
H = [int(i) for i in input().split()]
mh = max(H)
h = [0]*(mh+1)
ar = 0
for i in H:
    if h[i] == 0:
        ar += 1
    else:
        h[i] -= 1
    h[i-1] += 1
print(ar)