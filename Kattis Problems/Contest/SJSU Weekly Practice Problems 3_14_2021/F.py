n = int(input())
prev = 1
for _ in range(n):
    a,op,b = input().split()
    a,b = [int(i) for i in [a,b]]
    if op == "+":
        result = a + b - prev
    elif op == "-":
        result = (a - b) * prev
    elif op == "*":
        result = (a * b)**2
    elif op == "/":
        result = (a+1)//2
    print(result)
    prev = result