n = 600851475143
i = 1
while i*i < n:
    if n%i==0:
        n //= i
    i += 2
print(n)