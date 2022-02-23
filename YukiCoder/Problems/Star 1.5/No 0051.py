W = int(input())
D = int(input())
l = 0
while W != 0:
    l = W/(D**2)
    W -= l//1
    D -= 1
    # print(W,l)
print(int(l))