while True:
    try:
        n = int(input())
    except:
        break

    ln = len(str(n))
    num = "1"*ln
    while int(num) % n != 0:
        print(len(num), int(num) % n)
        num += "1"
    print(len(num))