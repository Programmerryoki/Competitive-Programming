# from decimal import Decimal, getcontext

# getcontext().prec = 10
N = int(input())
for _ in range(N):
    x0, y0 = [float(i) for i in input().split()]
    A = lambda x0,x1,y0,y1: [y0-y1, x1-x0, x0*(y0-y1)+y0*(x1-x0)]
    B = lambda x0,x2,y0,y2: [y0-y2, x2-x0, x0*(y0-y2)+y0*(x2-x0)]
    # y1t = (Decimal(str(2*y0)) + (Decimal(str(y0**2 - 4*(x0**2+y0**2)*(-x0**2+1)))).sqrt()) / Decimal(str((2*(x0**2+y0**2))))
    y1 = (2*y0 + (4*y0**2 - 4*(x0**2+y0**2)*(-x0**2+1))**0.5) / (2*(x0**2+y0**2))
    y2 = (2*y0 - (4*y0**2 - 4*(x0**2+y0**2)*(-x0**2+1))**0.5) / (2*(x0**2+y0**2))
    # print(y1, y2)
    if x0 != 0:
        x1 = (1 - y0*y1) / x0
        x2 = (1 - y0*y2) / x0
        print("(" + ",".join(map(lambda x: str(float(-x)), A(x0,x1,y0,y1) + B(x0,x2,y0,y2))) + ")")
    else:
        if y0 - y1 == 0:
            print("(0,")
        else:
            print("(" + ",".join(map(lambda x: str(float(-x)), A(0,0,y0,y1) + B(0,0,y0,y2))) + ")")