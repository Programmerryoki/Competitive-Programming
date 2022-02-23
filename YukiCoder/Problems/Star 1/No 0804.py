a,b,c,d = [int(i) for i in input().split()]
e = 0
v = 0
m = 0
while e + (c+1) <= d and v + 1 <= a and m + c <= b:
    e += c+1
    v += 1
    m += c
print(v)