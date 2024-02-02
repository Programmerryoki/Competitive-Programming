g = 21
n = [1]*g
for i in range(g-1):
    n2 = [0]*g
    for j in range(g):
        n2[j] = n[j] + (n2[j-1] if j>0 else 0)
    n = n2
print(n[-1])