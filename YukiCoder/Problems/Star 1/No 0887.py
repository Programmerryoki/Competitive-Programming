n = int(input())
ma = n
c = 0
while n != 1:
    if n%2==0:
        n = n//2
    else:
        n = 3*n + 1
        if n > ma:
            ma = n
    c += 1
print(c)
print(ma)