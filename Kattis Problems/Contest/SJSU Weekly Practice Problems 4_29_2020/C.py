n = int(input())
for _ in range(n):
    s,d = [int(i) for i in input().split()]
    if s < d:
        print("impossible")
    elif s%2 != d%2:
        print("impossible")
    else:
        a = (s + d)//2
        b = s - a
        print(a, b)