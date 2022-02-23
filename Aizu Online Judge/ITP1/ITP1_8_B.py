while True:
    s = 0
    num = int(input())
    if num == 0:
        break
    while num != 0:
        s += num%10
        num //= 10
    print(s)