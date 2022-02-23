case = 1
while True:
    try:
        x,y,r = map(float, input().split())
    except:
        break

    z = complex(0, 0)
    c = complex(x, y)
    div = False
    for i in range(int(r)+1):
        if abs(z) > 2:
            div = True
            break
        z = z*z + c
    print("Case "+str(case)+":","OUT" if div else "IN")
    case += 1