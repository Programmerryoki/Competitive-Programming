from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
ca = Counter(A)
total = 0
for num in ca:
    if ca[num] < num:
        total += ca[num]
    else:
        total += ca[num] - num
print(total)