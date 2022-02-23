from sys import stdin

case = 1
for a in stdin:
    n = [float(i) for i in a.split()]
    inum = complex(n[0], n[1])
    r = n[2]
    z = complex(0,0)
    i = 0
    while i < r and (z.imag**2 + z.real**2)**0.5 < 2:
        #print(i, z)
        z = z**2 + inum
        i += 1

    if i == r:
        print("Case " + str(case) + ": IN")
    else:
        print("Case " + str(case) + ": OUT")

    case += 1