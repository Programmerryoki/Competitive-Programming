from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i)-1 for i in input().split()]
CA = Counter(A)
CB = {}
for i,b in enumerate(B):
    if b in CB:
        CB[b].append(i)
    else:
        CB[b] = [i]
CC = Counter(C)
# print(CA,CB,CC)
total = 0
for keyA in CA:
    if keyA in CB:
        for j in CB[keyA]:
            if j in CC:
                total += CA[keyA] * CC[j]
print(total)