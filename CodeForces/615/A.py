t = int(input())
for i in range(t):
    a,b,c,n = [int(i) for i in input().split()]
    m = max(a,b,c)
    av = m * 3 - (a + b + c)
    if av <= n and (n-av)%3==0:
        print("YES")
    else:
        print("NO")