n = int(input())
a = 1
for i in range(1, n+1):
    print(i,a)
    if a <= i:
        a += i
    else:
        a -= i