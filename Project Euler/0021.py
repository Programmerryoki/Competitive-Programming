from functools import lru_cache

@lru_cache(None)
def d(n):
    s = 0
    for i in range(1, n):
        if n%i==0:
            s += i
    return s

s = 0
for n in range(1, 10001):
    if d(d(n)) == n and n != d(n):
        s += n
        print(n)
print(s)