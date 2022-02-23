a,b = [int(i) for i in input().split()]
if a == b:
    print(0)
else:
    print("+"+str(b-a) if b - a > 0 else "-"+str(a-b))