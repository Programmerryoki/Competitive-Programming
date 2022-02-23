n,a,b = [int(i) for i in input().split()]
if a > 0:
    d = n//(a+b)
    r = n-d*(a+b)
    print(d*a+min(r,a))
else:
    print(0)