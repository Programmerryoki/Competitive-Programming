N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
# total = [{}]
# for a in A:
#     t = dict(total[-1])
#     if a in t:
#         t[a] += 1
#     else:
#         t[a] = 1
#     total.append(t)

maxl = 0
d = {}
cur = 0
j = 0
for i in range(len(A)):
    cur += 1
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1
    if len(d) <= K:
        if cur > maxl:
            maxl = cur
    while len(d) > K:
        cur -= 1
        d[A[j]] -= 1
        if not d[A[j]]:
            del d[A[j]]
        j += 1
print(maxl)