N = int(input())
A = [int(i) for i in input().split()]
X = 0
for i in range(30):
    X = X + A[X%N]
    print(X,X%N)