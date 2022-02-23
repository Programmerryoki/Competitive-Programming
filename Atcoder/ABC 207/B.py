A,B,C,D = [int(i) for i in input().split()]
low = 0
high = 10**10
for _ in range(100):
    i = (low + high) // 2
    if C * i * D >= A + B * i:
        high = i
    else:
        low = i
print(high if high != 10**10 else -1)