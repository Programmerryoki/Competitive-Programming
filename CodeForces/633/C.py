t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = []
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            d.append(a[i+1])