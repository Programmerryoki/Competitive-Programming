X, Y = [int(i) for i in input().split()]
print("possible") if (X*4 + Y*3) % 2 == 0 else print("impossible")