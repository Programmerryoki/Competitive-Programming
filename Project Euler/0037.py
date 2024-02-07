lim = 2*10**7
primes = [1] * lim
primes[0] = 0
primes[1] = 0
for i in range(2,lim):
    if not primes[i]:
        continue
    for j in range(2*i, lim, i):
        primes[j] = 0

def trunc(n):
    s = str(n)
    for i in range(len(s)):
        # print(int(s[i:]), int(s[:len(s)-i]))
        if not primes[int(s[i:])] or not primes[int(s[:len(s)-i])]:
            return False
    return True


s = []
for i in range(10,lim):
    if not primes[i]:
        continue
    if trunc(i):
        print(i)
        s.append(i)
print(s)
print(len(s), sum(s))