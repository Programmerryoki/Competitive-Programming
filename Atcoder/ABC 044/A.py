N = int(input())
K = int(input())
X = int(input())
Y = int(input())

total = 0
if N <= K:
    total += X*N
else:
    total += X*K
    total += Y*(N - K)
print(total)