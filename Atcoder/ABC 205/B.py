from collections import Counter

N = int(input())
A = Counter([int(i) for i in input().split()])
print("Yes" if A == Counter([i for i in range(1,N+1)]) else "No")