ave = 0
stock = 0

while True:
    op, *n = input().split()
    if op == "buy":
        ave = (ave*stock + int(n[0])*int(n[1]))/(int(n[0])+stock)
        stock += int(n[0])
    elif op == "sell":
        stock -= int(n[0])
    elif op == "split":
        stock *= int(n[0])
        ave /= int(n[0])
    elif op == "merge":
        stock //= int(n[0])
        ave *= int(n[0])
    else:
        if ave > int(n[0]):
            print(stock*int(n[0]))
        else:
            print(stock*(int(n[0]) - (int(n[0]) - ave)*0.3))
        break
    # print(stock, ave)