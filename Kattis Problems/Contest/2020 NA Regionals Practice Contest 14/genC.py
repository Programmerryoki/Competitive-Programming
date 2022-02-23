from random import randint
n = randint(4, 6)
print(n)
lst = [randint(0,100) for i in range(n)]
print(" ".join(map(str, lst)))
print("NO" if sum(lst)&1 else "Yes")