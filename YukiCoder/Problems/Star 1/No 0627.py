T = int(input())
p = 0
for i in range(T):
    n = int(input())
    if abs(p - n) != 1:
        print("F")
        break
    p = n
else:
    print("T")