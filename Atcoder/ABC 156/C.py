N = int(input())
X = [int(i) for i in input().split()]
cost = float("inf")
for i in range(1,101):
    c = 0
    for j in X:
        c += (j - i)**2
    cost = min(cost, c)
print(cost)