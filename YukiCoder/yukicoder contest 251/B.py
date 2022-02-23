from collections import Counter
N,K,X,Y = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
RH = {}
for i in A:
    n = int((i-1+K-1)//K)
    if n != 0:
        try:
            RH[n] += 1
        except:
            RH[n] = 1
# RH = [int((i-1+K-1)//K) for i in A if int((i-1+K-1)//K) != 0]
if len(RH)*X <= Y:
    print(sum(RH.values()))
else:
    rh = Counter(RH)
    vals = rh.most_common()[::-1]
    print(vals)
    mi = min(RH.values)
    K = 0
    t = 0
    while True:
        K += mi*Y
        t += mi
