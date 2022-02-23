def pop(bal, bu):
    for bullet in bu:
        c = 0
        # breaking down coordinates and the vector of the bullet
        x0, y0, z0, bx, by, bz = bullet
        i = 0
        while i < len(bal):
            # ba is the balloons informations

            ba = bal[i]

            # breaking down coordinates of the balloon

            x1 = ba[2]
            y1 = ba[3]
            z1 = ba[1] + ba[0]

            # vector from bullets starting point to balloon's center point

            buToBa = [x1-x0, y1-y0, z1-z0]

            # the normal / length of the bullets vector

            b = (bx**2 + by**2 + bz**2)**0.5

            # the area of the parallelogram
            #  - calculated with the cross product between vector of the bullet and
            #    the vector from bullets starting point to the balloon's center point

            A = ((by * buToBa[2] - bz*buToBa[1])**2 + (bx*buToBa[2] - buToBa[0]*bz)**2 + (bx*buToBa[1] - by*buToBa[0])**2)**0.5

            # calculates the height of the parallelogram, which equals the
            # shortest distance between center of the balloon and the line
            # that the bullet goes through

            h =A/b

            # calculates the angle between the 2 vectors using the dot product
            # Function
            #
            #    a ・ b = |a| x |b| x cos(theta)
            #
            #                   a ・ b
            #    cos(theta) = -----------
            #                 |a| x |b|
            #
            # thus it will give negative value if the angle is obtuse
            # and potive value if the angle is acute

            angle = (bx*buToBa[0]+by*buToBa[1]+bz*buToBa[2])/(b * (buToBa[0]**2 + buToBa[1]**2 + buToBa[2]**2)**0.5)

            # simple conditions to check if the shortest distance from the bullets path
            # to balloon is smaller than the radius. If so, the bullet pops the balloon
            if h <= ba[0] and angle >= 0:
                c += 1
                bal.pop(i)
            else:
                i += 1

        print(c)

##########
# inputs #
##########
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

    pop(balloons, bullets)