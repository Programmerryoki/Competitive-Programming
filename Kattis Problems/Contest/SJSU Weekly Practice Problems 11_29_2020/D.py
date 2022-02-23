from math import atan,degrees

while True:
    a,b,s,m,n = map(int, input().split())
    if [a,b,s,m,n].count(0) == 5:
        break
    w = a*m; h = b*n
    dis = (w**2 + h**2)**0.5
    print("{:.2f} {:.2f}".format(90 - round(degrees(atan(w / h)), 2), round(dis / s, 2)))