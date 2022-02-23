n = int(input())
p = 2
for a in range(n):
    p += p-1
print(p**2)