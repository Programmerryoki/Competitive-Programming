def collatz(n):
    d = 1
    while n > 1:
        n = 3*n+1 if n&1 else n//2
        d += 1
    return d

md = 0
for n in range(1, 1000000):
    c = collatz(n)
    if c >= md:
        md = c
        print(c, n)