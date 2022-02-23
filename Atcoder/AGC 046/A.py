X = int(input())
n = 360
c = 0
while True:
    c += n // X
    n %= X
    if n == 0:
        break
    n += 360
print(c)