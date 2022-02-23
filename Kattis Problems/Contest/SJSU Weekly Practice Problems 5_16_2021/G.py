from decimal import Decimal

N,Q = map(int, input().split())
tempe = []
for _ in range(N):
    a,b = map(int, input().split())
    tempe.append((a,Decimal(b-a)/100))
print(tempe)
for _ in range(Q):
    x,y,v = map(int, input().split())
    zx, tx = tempe[x-1]
    zy, ty = tempe[y-1]

    celsius = (v - zx) / tx
    c,d = (zy + ty * celsius).as_integer_ratio()
    print(str(c)+"/"+str(d))