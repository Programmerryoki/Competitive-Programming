total = 0
n = 1
d = 2
c = 0
size = 1001
while n < size**2 + 1:
    total += n
    n += d
    c += 1
    if c == 4:
        c = 0
        d += 2
print(total)