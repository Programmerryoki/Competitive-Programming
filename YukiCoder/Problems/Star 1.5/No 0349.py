from collections import Counter

N = int(input())
A = Counter()
for _ in range(N):
    s = input()
    A.setdefault(s, 0)
    A[s] += 1
if A.most_common(1)[0][1] > (N+1)/2:
    print("NO")
else:
    print("YES")