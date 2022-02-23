s = int(input())
pos = {s}
c = 0
n = s
while True:
    n = 3*n+1 if n&1 else n//2
    c += 1
    if n in pos:
        print(c+1)
        break
    pos.add(n)