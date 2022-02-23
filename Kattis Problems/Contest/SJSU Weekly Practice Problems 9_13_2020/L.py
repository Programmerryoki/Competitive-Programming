n, X = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
P.sort()
if len(P) == 1:
    print(1)
    exit()
for i in range(n-1):
    if P[i] + P[i+1] > X:
        print(i+1)
        exit()
print(len(P))