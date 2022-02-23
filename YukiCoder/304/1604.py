N = int(input())
P = [int(i) for i in input().split()]
total = 0
for i in range(N, 0, -1):
    ind = P.index(i)
    total += i - ind - 1
    P = P[:ind] + P[ind+1:]
print(total)