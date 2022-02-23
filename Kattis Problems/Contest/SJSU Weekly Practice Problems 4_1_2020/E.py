n, p, d = [int(i) for i in input().split()]
r = input()*2
c = 0
for i in range(p-1, p-1+n):
    if r[i:i+p].count("Z") < d:
        c += 1
print(c)