line = input()
while line != "0":
    x1, y1, x2, y2, p = [float(i) for i in line.split()]
    print((abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p))
    line = input()