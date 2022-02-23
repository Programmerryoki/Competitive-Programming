from sys import stdin

input =
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    seen = set()
    order = []
    while True:
        ts = tuple(A)
        if ts in seen:
            break
        order.append(ts)
        seen.add(ts)
        cb = {}
        for val in A:
            if val not in cb:
                cb[val] = 0
            cb[val] += 1
        for i in range(n):
            A[i] = cb[A[i]]
    q = int(input())
    ans = []
    for _ in range(q):
        x,k = [int(i) for i in input().split()]
        # print(order[min(k, len(order)-1)])
        ans.append(order[min(k, len(order)-1)][x-1])
    print("\n".join(map(str, ans)))