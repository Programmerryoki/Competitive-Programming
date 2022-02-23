N = int(input())
A = [int(i) for i in input().split()]
count = {}
for a in A:
    if a not in count:
        count[a] = 0
    count[a] += 1
for c in count:
    if count[c] == 3:
        print(c)