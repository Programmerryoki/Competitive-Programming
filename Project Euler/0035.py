lim = 10**7
primes = [1]*lim
primes[0] = 0
primes[1] = 0
for i in range(2,lim):
    if not primes[i]:
        continue
    for j in range(2*i, lim, i):
        primes[j] = 0

def circular(n):
    for i in range(len(n)):
        if not primes[int(n[i:] + n[:i])]:
            return False
    return True

s = set()
for n in range(1,10**6):
    if circular(str(n)):
        s.add(n)
        print(n)
print(len(s))