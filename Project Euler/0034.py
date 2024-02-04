from math import factorial

total = 0
for n in range(3,factorial(10)+1):
    if n == sum(factorial(int(i)) for i in str(n)):
        print(n)
        total += n
print(total)