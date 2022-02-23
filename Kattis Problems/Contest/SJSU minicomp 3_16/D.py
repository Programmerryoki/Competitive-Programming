a = [int(i) for i in input().split()]
a.sort()
b = [a[i+1] - a[i] for i in range(2)]
if b[0] > b[1]:
    print((a[0] + a[1]) //2)
elif b[0] < b[1]:
    print((a[1] + a[2]) // 2)
else:
    print(a[-1] + b[-1])