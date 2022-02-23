a,b,c,n = [int(i) for i in input().split()]
if a == 0 or b == 0 or c == 0 or n < 3 or a+b+c < n:
    print("NO")
else:
    print("YES")