M = int(input())
n = 1
for i in range(1, 129):
    n = (n*2) % M
print(n)