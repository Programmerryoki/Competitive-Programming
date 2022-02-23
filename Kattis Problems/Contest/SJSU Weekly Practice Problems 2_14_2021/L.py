for a in range(1,101):
    for b in range(1,6,2):
        print(a,b,sum([i**b for i in range(1,a+1)])%a)

a,b = map(int, input().split())
if a&1:
    print(0)
elif a%4:
    print(a//2)
else:
    print(a//2 if b == 1 else 0)