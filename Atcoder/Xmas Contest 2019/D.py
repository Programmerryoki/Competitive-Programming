n = int(input())
prime = [1 for i in range(n+1)]
prime[0] = 0
prime[1] = 0
i = 0
while True:
    try:
        i = prime.index(1,i+1)
        for a in range(i,n+1,i):
            prime[a] = 0
        c = 0
        num = i
        while num <= n:
            c += n//num
            num *= i
        prime[i] = c
        # print(i,prime)
    except:
        break
print([i for i in range(1,n+1)])
print(prime[1:])

answer = []
for z in range(1,n+1):
    t = 0
    for a in range(1,z+1):
        c = 0
        num = a
        i = 2
        while num != 1:
            count = num
            while num%i == 0:
                num //= i
                c += 1
            i += 1
        # print(a,c)
        t += (-1)**c
    answer.append(t)
print()
print([i for i in range(1,n+1)])
print(answer)