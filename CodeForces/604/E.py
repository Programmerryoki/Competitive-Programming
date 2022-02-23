n = int(input())
p = [int(i) for i in input().split()]
q = [100-i for i in p]
# print(p,q)

m = []
mul = 1
t = 0
for a in range(n):
    num = mul * q[a] * (a + 1)
    m.append(num)
    t += num
print(m,t)