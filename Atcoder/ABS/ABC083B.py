N,A,B = [int(i) for i in input().split()]
tn = 0
for n in range(1, N+1):
    if A <= sum(int(i) for i in str(n)) <= B:
        tn += n
print(tn)