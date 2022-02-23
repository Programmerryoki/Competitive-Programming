N,A,B = [int(i) for i in input().split()]
ts = 0
for n in range(1,N+1):
    s = sum([int(i) for i in str(n)])
    if A <= s <= B:
        ts += n
print(ts)