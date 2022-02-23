primes = set()
for num in range(2, 202):
    for p in primes:
        if num%p==0:
            break
    else:
        primes.add(num)

A,B,C,D = [int(i) for i in input().split()]
md = [0]*(B-A+1)
for num in range(A, B+1):
    for i in range(num+C, num+D+1):
        if i in primes:
            break
    else:
        print("Takahashi")
        exit()
print("Aoki")