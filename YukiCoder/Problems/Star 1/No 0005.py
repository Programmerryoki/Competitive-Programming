L = int(input())
N = int(input())
W = [int(i) for i in input().split()]
W.sort()
t = 0
i = 0
while i < N and t + W[i] <= L:
    t += W[i]
    i += 1
print(i)