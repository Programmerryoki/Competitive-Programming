n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

d = 0
for i in range(n):
    d += abs(x[i] - y[i])
print(d)

d = 0
for i in range(n):
    d += (x[i] - y[i])**2
print(d**0.5)

d = 0
for i in range(n):
    d += (abs(x[i] - y[i]))**3
print(d**(1/3))

print(max([abs(x[i] - y[i]) for i in range(n)]))