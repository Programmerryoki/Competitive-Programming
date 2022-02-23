import heapq

N = int(input())
C = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]
mhp = []
cp = 0
cost = 0
for i in range(N-1):
    heapq.heappush(mhp, [C[i], i])
    print(mhp, cp, i, cost)
    cost += mhp[0][0] * (T[i+1] - T[i] + ((T[i+1]-T[i])%2 == 0))
    print(cost)
    if cp != mhp[0][1]:
        cost += sum(C[cp:mhp[0][1]+1])
        cp = mhp[0][1]
print(cost)