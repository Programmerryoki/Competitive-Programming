l, n = [int(i) for i in input().split()]
t = n
c = 1
while True:
    if t == 0 or l%t == 0:
        break
    t = t - l%t
    c += 1
print(c)