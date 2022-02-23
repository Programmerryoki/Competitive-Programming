from collections import Counter

N = int(input())
D = [int(i) for i in input().split()]
CD = Counter(D)
M = int(input())
T = [int(i) for i in input().split()]
CT = Counter(T)
for key in CT:
    if key not in CD or CT[key] > CD[key]:
        print("NO")
        exit()
print("YES")