N,M = [int(i) for i in input().split()]
c = 0
for i in range(N):
    c += input().count("W")
print(c)