a, b = 1,1
n = 1
while len(str(a)) < 1000:
    n += 1
    a, b = b, a+b
print(n, a)