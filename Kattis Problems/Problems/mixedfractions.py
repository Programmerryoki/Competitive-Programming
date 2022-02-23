from sys import stdin
for s in stdin:
    n, d = [int(i) for i in s.split()]
    if n == 0 and d == 0:
        break
    print(n//d, n%d, "/", d)