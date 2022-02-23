N,K = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

dic = {}
md = 0
d = 0
count = 0
for i,c in enumerate(C):
    count += 1
    if count > K:
        # print(i, K, i-K)
        dic[C[i - K]] -= 1
        if dic[C[i - K]] == 0:
            d -= 1
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
    if dic[c] == 1:
        d += 1
    md = max(md, d)
print(md)