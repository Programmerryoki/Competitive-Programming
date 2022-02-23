N = int(input())
cups = [0]*3
cups[N-1] += 1
M = int(input())
for _ in range(M):
    p,q = [int(i)-1 for i in input().split()]
    cups[p], cups[q] = cups[q], cups[p]
print(cups.index(1)+1)