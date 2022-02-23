n = int(input())
prev = 1
for i in range(n):
    a,op,b = input().split()
    a = int(a)
    b = int(b)
    if op == "+":
        prev = (a+b) - prev
    elif op == "-":
        prev *= (a-b)
    elif op == "*":
        prev = (a*b)**2
    elif op == "/":
        prev = int((a + 1) // 2) if a&1 else int(a // 2)
    print(prev)