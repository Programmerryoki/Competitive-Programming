def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for a in range(2,int(n**0.5)+1):
        if n%a==0:
            return False
    return True

T = int(input())
for a in range(T):
    n, m = [int(i) for i in input().split()]
    num = m
    path = []
    if isPrime(m):
        while m not in path and m != 1:
            path.append(m)
            m = sum(map(lambda x: int(x)**2, list(str(m))))
        if m == 1:
            print(n, num, "YES")
            continue
    print(n, num, "NO")