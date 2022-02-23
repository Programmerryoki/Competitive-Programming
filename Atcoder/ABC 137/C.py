from collections import Counter

N = int(input())
s = [tuple(sorted(Counter(input()).most_common())) for i in range(N)]
sc = Counter(s)
total = 0
for key, val in sc.most_common():
    total += int((val) * (val-1) / 2)
print(total)