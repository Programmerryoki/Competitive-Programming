from random import randint, shuffle

t = randint(3,3)
print(t)
for _ in range(t):
    n = randint(4, 8)
    print(n)
    tmp = [0] * (n//2) + [1] * (n//2) + [1] * (n&1)
    shuffle(tmp)
    print(" ".join(map(str, tmp)))