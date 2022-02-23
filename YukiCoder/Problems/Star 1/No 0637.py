a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a[i]%3 == 0 and a[i]%5 == 0:
        a[i] = 8
    elif a[i]%3 == 0 or a[i]%5 == 0:
        a[i] = 4
    else:
        a[i] = len(str(a[i]))
print(sum(a))