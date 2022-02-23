n = int(input())
a = 1
for i in range(2,int(n**0.5)+1):
    while n%(i**2)==0:
        n //= i**2
        a *= i
print(a,n)