from math import ceil
N,X,T = map(int, input().split())
print(T * ceil(N / X))