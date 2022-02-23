N = int(input())
K = int(input())
X = [int(i) for i in input().split()]
tc = 0
for i,x in enumerate(X):
    tc += min(abs(K - x), x)*2
print(tc)