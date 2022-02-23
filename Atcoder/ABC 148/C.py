b,a = [int(i) for i in input().split()]
c,d = b,a
while a%b!= 0:
    # print(a,b,a%b)
    a, b = b, a%b
print(c//b*d//b*b)