s,t,n = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

for i in range(n):
    s += d[i]
    s = ((s + c[i] - 1)//c[i]) * c[i]
    s += b[i]
s += d[-1]
print("yes" if s <= t else "no")