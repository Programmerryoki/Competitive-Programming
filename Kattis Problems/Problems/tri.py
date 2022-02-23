n = list(map(int, input().split()))
a = n[0]
b = n[1]
c = n[2]
if a + b == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"+"+b+"="+c)
elif a - b == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"-"+b+"="+c)
elif a * b == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"*"+b+"="+c)
elif a / b == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"/"+b+"="+c)
elif a == b + c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"="+b+"+"+c)
elif a == b - c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"="+b+"-"+c)
elif a == b * c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"="+b+"*"+c)
elif a == b / c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a+"="+b+"/"+c)