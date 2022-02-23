from math import log, ceil

X = int(input())
i = 0
n = 100
while X > n:
    n = int(1.01 * n)
    i += 1
print(i)