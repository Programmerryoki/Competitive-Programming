a,b,c,d = [int(i) for i in input().split()]
t = 0
for i in range(a,b+1):
    if c <= i <= d:
        t += d-c
    else:
        t += d-c+1
print(t)