from math import pi

t = int(input())
for _ in range(t):
    r,n = [int(i) for i in input().split()]
    td = 0
    cd = [int(i) for i in input().split()]
    ini = [i for i in cd]
    for i in range(n-1):
        x,y = [int(i) for i in input().split()]
        td += ((cd[0] - x)**2+(cd[1] - y)**2)**0.5
        cd = [x,y]
    td += ((ini[0] - cd[0])**2+(ini[1] - cd[1])**2)**0.5
    if (td - 2*pi*r) < 0:
        print("Not possible")
    else:
        print((td-2*pi*r)/td)