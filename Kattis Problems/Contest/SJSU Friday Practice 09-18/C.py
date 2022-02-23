while True:
    try:
        a,b = [int(i) for i in input().split()]
    except:
        break

    print(abs(a-b))