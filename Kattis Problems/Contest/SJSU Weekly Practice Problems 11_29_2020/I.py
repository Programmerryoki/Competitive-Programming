n = N = int(input())
fact = 0
i = 2
while n != 1 and i**2 <= N:
    while n%i == 0:
        n //= i
        fact += 1
    i += 1
if n != 1:
    fact += 1
print(fact)