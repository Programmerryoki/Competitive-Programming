a,b = [int(i) for i in input().split()]
d = [i for i in range(a,b+1)]
c = 3
if 23 in d:
    c -= 1
if 24 in d:
    c -= 1
if 25 in d:
    c -= 1
print(c)