primes = [2]
for num in range(3, 10**3):
    for p in primes:
        if num%p==0:
            break
    else:
        primes.append(num)

N,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
used = set()
for a in A:
    for p in primes:
        if p**2 > a:
            if a != 1:
                used.add(a)
            break
        if a%p==0:
            used.add(p)
            while a%p==0:
                a //= p

count = [1]*(M+1)
for p in sorted(used):
    for j in range(p, len(count), p):
        count[j] = 0
ans = []
for i in range(1,len(count)):
    if count[i] == 1:
        ans.append(i)
print(len(ans))
print("\n".join(str(i) for i in ans))