from collections import Counter
S = Counter(input())
c = 0
for k,n in S.most_common():
    if c == 6:
        if n == 1:
            print(k)
            break
    if n == 2:
        c += 1
else:
    print("Impossible")