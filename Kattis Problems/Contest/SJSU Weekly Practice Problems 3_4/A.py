from math import factorial

N = int(input())
print(factorial(N)//(factorial(2)*factorial(N-2)))