n = int(input())
v = [int(i) for i in input().split()]
l = 0
r = False
for i in range(n-1):
    if v[i] > v[i+1]:
        r = True
    elif v[i] < v[i+1]:
        l = i
        if r:
