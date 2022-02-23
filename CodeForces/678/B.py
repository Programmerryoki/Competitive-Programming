primes = [2]
for i in range(3,202):
    for p in primes:
        if i%p == 0:
            break
    else:
        primes.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    for p in primes:
        if p > n:
            pri = p - n + 1
            if pri in primes:
                continue
            else:
                break
    col = [1 for i in range(n-1)] + [p - n + 1]
    for i in range(n):
        print(" ".join(map(str, col[i:] + col[:i])))