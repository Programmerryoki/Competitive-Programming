N,K = [int(i) for i in input().split()]
can = [0]*N
for _ in range(K):
    d = int(input())
    A = [int(i) for i in input().split()]
    for a in A:
        can[a-1] += 1
print(can.count(0))