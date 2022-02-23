from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
ca = Counter(A)
ts = 0
for k in ca:
    ts += (ca[k] * (ca[k] - 1)) // 2
ans = [0]*N
for i,a in enumerate(A):
    ans[i] = ts - (ca[a] - 1)
print("\n".join(map(str, ans)))