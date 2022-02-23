from random import randint
N = randint(1, 2001)
print(N)
for _ in range(N):
    print(randint(-10000, 10001), randint(-10000, 10001), randint(1, 10001))