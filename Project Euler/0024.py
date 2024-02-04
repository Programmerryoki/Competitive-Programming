from itertools import permutations

n = 10
m = 1000000
print(list(permutations(range(n), n))[1000000 - 1])