from collections import Counter

N = int(input())
C = {}
for _ in range(N):
    n = len(input()) - 2
    C.setdefault(n, 0)
    C[n] += 1
ans = list(Counter(C).most_common())
ans.sort(key = lambda x: (x[1], x[0]), reverse=True)
print(ans[0][0])