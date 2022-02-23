c = int(input())
for a in range(2,int(c**0.5)+1):
    if c%a==0:
        print(a,c//a)
        break
else:
    print(1,c)