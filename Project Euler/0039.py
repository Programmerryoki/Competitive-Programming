mpc = 0
mp = 0
for p in range(3,1001):
    pc = 0
    for a in range(1,p):
        for b in range(a,p):
            c = p-a-b
            if not c >= b >= a:
                break
            if a**2 + b**2 == c**2 and a+b > c:
                # print(a,b,c)
                pc += 1
    if mpc < pc:
        mpc = pc
        mp = p
        print(mp, mpc)