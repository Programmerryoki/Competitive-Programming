a,b,c = [int(i) for i in input().split()]
m = 0
while True:
    if c-b==1 and b-a==1:
        break
    if c-b > b-a:
        a,b = b,b+1
    else:
        c,b = b,b-1
    m += 1
print(m)