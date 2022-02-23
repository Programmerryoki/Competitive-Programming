A,B = [int(i) for i in input().split()]
t = A + B
print((t + B)//3 - (t + A - 1)//3)