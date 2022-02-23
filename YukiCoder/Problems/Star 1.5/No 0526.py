N,M = [int(i) for i in input().split()]
f1, f2 = 0, 1
for _ in range(N-1):
    f1,f2 = f2, (f1+f2)%M
print(f1)