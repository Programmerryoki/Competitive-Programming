a,b,c,d = [int(i) for i in input().split()]
# Ax^2+Bx+C
# A(x^2+B/Ax)+C
# A(x^2+B/Ax+(B/2A)^2)+C-(B/2A)^2
# A(x+(B/2A))^2+C-(B/2A)^2
heihou = lambda a,b,c: [a,b/(2*a),c - ((b**2)/(4*a))]
Y1 = lambda x: x^2+a*x+b
Y2 = lambda x: -x^2+c*x+d
C1 = heihou(1,a,b)
C2 = heihou(-1,c,d)
Y = heihou(2,a-c,b-d)
# 2x^2+(a+c)x+(b+d)
# 0 = A(x+B)^2+C
# -C/A = (x+B)^2
# (-C/A)**0.5 = x+B
P = lambda p : [(-p[2]/p[0])**0.5 - p[1], -(-p[2]/p[0])**0.5 - p[1]]
YP = P(Y)
print(C1,C2)
print(YP)
if C1[-1] > C2[-1]:
    print("No")
elif C1[-1] == C2[-1]:
    print("Yes")
else:
    p = (Y1(YP[0]) - Y1(YP[1])) / (YP[0] - YP[1])
    mx = min(YP)

    print(p)