from collections import Counter
N = int(input())
ac = Counter([int(i) for i in input().split()])
c = 0
for k in ac.keys():
    if ac[k] == 1:
        c += 1
print(c)