from itertools import accumulate

T = int(input())
for _ in range(T):
    N = int(input())
    customers = []
    for _ in range(N):
        W,*res = [int(i) for i in input().split()]
        customers.append(sum(res))
    customers.sort()
    print(sum(accumulate(customers)) / len(customers))