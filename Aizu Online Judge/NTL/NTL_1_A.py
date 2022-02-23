n = a = int(input())
prime = [2]
pf = []
i = 2
while n != 1:
    while n%i == 0:
        pf.append(i)
        n //= i
    while True:
        for p in prime:
            if i%p==0:
                break
        else:
            prime.append(i)
            break
        i += 1
        if i > int(n**0.5)+1:
            if n == 1:
                break
            pf.append(n)
            n = 1
            break
print(str(a)+": "+" ".join(map(str, pf)))