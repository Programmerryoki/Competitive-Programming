from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
CA = Counter(A)
l = []
for key in sorted(CA, reverse=True):
    if CA[key] >= 2:
        if not l and CA[key] >= 4:
            print(key**2)
            exit()
        l.append(key)
        if len(l) >= 2:
            break
print(l[0]*l[1] if len(l) == 2 else 0)