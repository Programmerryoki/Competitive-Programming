from math import factorial as ft

N = int(input())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]

num = [1 for i in range(1,N+1)]
t1 = 0
for a in range(len(p)):
    t1 += ft(N-a-1)*num[:p[a]].count(1)
    num[p[a]-1] = 0
    # print(N-a-1, t1,num)
# print(t1)

num = [1 for i in range(1,N+1)]
t2 = 0
for a in range(len(q)):
    t2 += ft(N-a-1)*num[:q[a]].count(1)
    num[q[a]-1] = 0
    # print(N-a-1, t2,num)
# print(t2)
print(abs(t1-t2))