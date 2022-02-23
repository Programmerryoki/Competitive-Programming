from math import log10

n = int(input())
ln = len(str(n))
if ln < 4:
    print(1 if n == 1 else 2 if n==2 else 3 if n==6 else 4 if n==24 else 5 if n==120 else 6)
    exit()
num = log10(720)
i = 6
while True:
    i += 1
    num += log10(i)
    if num > ln:
        print(i-1)
        exit()