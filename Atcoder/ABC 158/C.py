a,b = [int(i) for i in input().split()]
for p in range(1,1251):
    if int(p*0.08) == a and int(p*0.1) == b:
        print(p)
        break
else:
    print(-1)