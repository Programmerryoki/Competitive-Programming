from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
CA = Counter(A)
total = 0
all = N
for key in CA:
    all -= CA[key]
    total += CA[key] * all
print(total)