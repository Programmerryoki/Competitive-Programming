A,B = [int(i) for i in input().split()]
if B == 1:
    print(0)
    exit()
c = 0
while True:
    B -= A
    c += 1
    if B <= 0:
        print(c)
        break
    B += 1