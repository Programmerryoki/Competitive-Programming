def pop(bal, bu):
    for bullet in bu:
        c = 0

        x0, y0, z0, bx, by, bz = bullet
        i = 0
        while i < len(bal):
            ba = bal[i]
            print(bullet, ba)
            x1 = ba[2]
            y1 = ba[3]
            z1 = ba[1] + ba[0]
            d = bx * x1 + by * y1 + bz * z1
            H = (d - (bx * x0 + by * y0 + bz * z0)) / (bx ** 2 + by ** 2 + bz ** 2)
            D = ((x0 + bx * H) - x1) ** 2 + ((y0 + by * H) - y1) ** 2 + ((z0 + bz * H) - z1) ** 2
            x = (x0 + bx * H)
            y = (y0 + by * H)
            z = (z0 + bz * H)

            if D <= ba[0] and H >= 0:
                c += 1
                bal.pop(i)
            else:
                i += 1

        print(c)


while True:
    cases = int(input())
    if cases == 0:
        break

    bullets = []
    balloons = []
    for asdsf in range(cases):
        balloons.append([float(i) for i in input().split()])

    cases = int(input())
    for asdfas in range(cases):
        bullets.append([float(i) for i in input().split()])

    # print(balloons)
    # print(bullets)
    pop(balloons, bullets)