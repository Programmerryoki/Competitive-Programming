t1, t2 = [int(i) for i in input().split()]
a1, a2 = [int(i) for i in input().split()]
b1, b2 = [int(i) for i in input().split()]


d1 = (a1 - b1)*t1
d2 = (a2 - b2)*t2
if d1 + d2 == 0:
    print("infinity")
else:
    if a1 > b1 and a2 > b2:
        print(0)
    elif a1 < b1 and a2 < b2:
        print(0)
    elif d1 + d2 < 0:
        print(0)
    else:
        print(abs(d2//(d1+d2))*2-1)