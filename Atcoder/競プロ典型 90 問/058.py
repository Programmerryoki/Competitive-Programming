N,K = [int(i) for i in input().split()]
order = [N]
seen = {N}
for i in range(K):
    N = (N + sum(int(str(j)) for j in str(N))) % 10**5
    if N in seen:
        break
    order.append(N)
    seen.add(N)
# print(order)
oin = order.index(N)
order = order[oin:]
print(order[(K-oin) % len(order)])