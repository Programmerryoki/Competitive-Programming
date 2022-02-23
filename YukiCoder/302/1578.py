MOD = 10**9 + 7

A,B,C = [int(i)%MOD for i in input().split()]
K = int(input())
order = [(A,B,C)]
count = {(A,B,C)}
for i in range(K):
    A,B,C = (B*C)%MOD, (A*C)%MOD, (A*B)%MOD
    tup = (A,B,C)
    if tup in count:
        order = order[order.index(tup):]
        break
    order.append(tup)
    count.add(tup)
A,B,C = order[K % len(order)]
print((((A*B)%MOD)*C)%MOD)