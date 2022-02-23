while True:
    x, y = [int(i) for i in input().split()]
    if x == 0 and y == 0:
        break
    if x > y:
        print(y,x)
    else:
        print(x,y)