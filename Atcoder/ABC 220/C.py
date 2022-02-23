N = int(input())
A = [int(i) for i in input().split()]
X = int(input())
cumsum = [A[0]]
for i in range(1, N):
    cumsum.append(cumsum[-1] + A[i])
total = (X // cumsum[-1]) * len(cumsum)
X %= cumsum[-1]
i = 0
while X > 0:
    X -= A[i]
    i += 1
print(total + i + (X == 0))