T = int(input())
for _ in range(T):
    n1 = int(input())
    a = [int(i) for i in input().split()]
    n2 = int(input())
    b = [int(i) for i in input().split()]
    ans = [0]*(n1 + n2 + 1)
    for i in range(n1+1):
        for j in range(n2+1):
            ans[i+j] += a[i]*b[j]
    print(n1+n2)
    print(" ".join(map(str, ans)))