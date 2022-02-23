t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    # print(a)
    count = 0
    for i in range(n-1):
        m = ((i+1) // a[i]) * a[i]
        for j in range(m, n + i + 1, a[i]):
            k = j+(a[i] - (i+1))-1
            # print(i,j,k,m, n+i)
            if i >= k:
                continue
            if k >= n:
                break
            if a[i]*a[k] == (i+k+2):
                count +=1
    print(count)