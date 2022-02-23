a,b = [int(i) for i in input().split()]
while a%b != 0:
    a, b = b, a%b
print(b)