N,K = map(int, input().split())
primes = [1]*(N+1)
count = 0
for n in range(2,N+1):
    for i in range(n,N+1,n):
        if primes[i] == 0:
            continue
        count += 1
        primes[i] = 0
        if count == K:
            print(i)
            exit()