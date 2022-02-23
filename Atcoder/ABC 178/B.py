a,b,c,d = [int(i) for i in input().split()]
if b > 0 and d > 0:
    print(max(b*d, a*c))
elif a < 0 and c < 0:
    print(max(b*d, a*c))
else:
    print(max(a*d, b*c))