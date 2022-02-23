a,b,c = [int(i) for i in input().split()]
print("Yes" if (a+b)//2==c or (a+c)//2==b or (b+c)//2==a else "No")