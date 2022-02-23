from collections import Counter
N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
ca = Counter(A)
count = [[k, ca[k]] for k in ca]
count.sort(key = lambda x: x[1])
tn = 0
for i in range(len(count) - K):
    tn += count[i][1]
print(tn)