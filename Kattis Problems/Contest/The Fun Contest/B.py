from random import randint

m = 99
total = 2
print(total)
while total < m:
    n = int(input())
    if n == m:
        break
    if n % 3 == 0:
        total = n + randint(1, 2)
    else:
        total = n + (3 - n % 3)
    print(total)
