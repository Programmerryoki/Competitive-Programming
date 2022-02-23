from collections import Counter

n = int(input())
a = [int(i) for i in input().split()]
ca = Counter(a)
for i in range(6,0,-1):
    if ca[i] == 1:
        print(a.index(i)+1)
        exit()
print("none")