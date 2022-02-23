N = int(input())
c = 0
for k in range(2,N+1):
    n = N
    while n >= k:
        if n%k==0:
            n //= k
        else:
            n = n - k
    if n == 1:
        c += 1
        print(k, N%k)
print("",c)