a,b,c = [int(i) for i in input().split()]
if a == b+c or b == a+c or c == a+b:
    print("Yes")
else:
    print("No")