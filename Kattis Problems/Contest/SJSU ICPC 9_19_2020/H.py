e,f,c = [int(i) for i in input().split()]
e += f
tb = 0
while e >= c:
    tb += e // c
    e = e%c + e//c
print(tb)