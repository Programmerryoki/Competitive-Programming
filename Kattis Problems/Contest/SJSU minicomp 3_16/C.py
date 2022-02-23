from itertools import permutations

primes = [1]*(10**7)
primes[0] = 0
primes[1] = 0
i = 0
while True:
    try:
        i = primes.index(1, i+1)
    except:
        break
    for a in range(i*2, len(primes), i):
        primes[a] = 0


t = int(input())
for _ in range(t):
    n = list(input())
    c = 0
    for a in range(1,len(n)+1):
        for b in permutations(n, a):
            num = int("".join(b))
            if len(str(num)) == a:
                if primes[num] == 1:
                    c += 1
    print(c)