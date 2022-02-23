n = int(input())
for a in range(n):
    num = input().split(" ")
    nAD = int(num[0])
    AD = int(num[1]) - int(num[2])
    if nAD < AD:
        print("advertise")
    elif nAD > AD:
        print("do not advertise")
    else:
        print("does not matter")