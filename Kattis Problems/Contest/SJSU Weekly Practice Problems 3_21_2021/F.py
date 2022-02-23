from collections import Counter

cinput = Counter(input())
total = 0
for key, val in cinput.items():
    total += val&1
print(max(0, total-1))