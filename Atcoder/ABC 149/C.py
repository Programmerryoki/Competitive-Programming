x = int(input())
while True:
    for a in range(2,int(x**0.5)):
        if x%a==0:
            break
    else:
        print(x)
        break
    x += 1