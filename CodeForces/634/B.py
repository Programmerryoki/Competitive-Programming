t = int(input())
for _ in range(t):
    n, a, b = [int(i) for i in input().split()]
    w = 0
    s = ""
    for i in range(b):
        s += chr(ord("a") + i)
    s += chr(ord("a")+b-1)*(a-b)
    s *= n//a
    s += s[:n-len(s)]
    print(s)