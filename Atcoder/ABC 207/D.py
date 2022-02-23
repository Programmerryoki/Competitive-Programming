from math import tan, atan, degrees, radians, sin, cos, acos

def translateArr(arr,dx,dy):
    return [(i[0]+dx, i[1]+dy) for i in arr]

def rotateArr(arr, angle):
    new = []
    for x,y in arr:
        new.append(rotate(x,y,angle))
    return new

def rotate(x,y,angle):
    dis = (x**2 + y**2)**0.5
    if x == 0 and y == 0:
        return (x, y)
    elif x == 0 or y == 0:
        if x == 0:
            if y < 0:
                ang = 270
            elif y > 0:
                ang = 90
        elif y == 0:
            if x < 0:
                ang = 180
            elif x > 0:
                ang = 0
    else:
        ang = degrees(atan(abs(y) / abs(x)))
        if y > 0 and x < 0:
            ang = 180 - ang
        elif y < 0 and x < 0:
            ang += 180
        elif y < 0 and x > 0:
            ang = 360 - ang
    # print(ang, x,y)
    ang = (ang + angle + 360) % 360
    # print(ang)
    if ang % 90 == 0:
        if ang == 0: return (dis, 0)
        if ang == 90: return (0, dis)
        if ang == 180: return (-dis, 0)
        if ang == 270: return (0, -dis)
    if ang < 90:
        calc = ang
    elif ang < 180:
        calc = 180 - ang
    elif ang < 270:
        calc = ang - 180
    elif ang < 360:
        calc = 360 - ang

    y = dis * sin(radians(calc))
    x = dis * cos(radians(calc))
    if ang < 90:
        return (x,y)
    elif ang < 180:
        return (-x,y)
    elif ang < 270:
        return (-x,-y)
    elif ang < 360:
        return (x, -y)

def distance(x,y,a,b):
    return ((x-a)**2 + (y-b)**2)**0.5

def anglefrom(x,y,a,b):
    A = distance(x,y,a,b)
    B = distance(0,0,x,y)
    C = distance(0,0,a,b)
    ang = acos((B**2 + C**2 - A**2) / (2 * B * C))
    if A**2 < B**2 + C**2:
        ang = degrees(ang)
    elif A**2 == B**2 + C**2:
        ang = 90
    elif A**2 > B**2 + C**2:
        ang = 180 - degrees(ang)
    if rotate(x,y,ang) == (a,b):
        return ang
    else:
        return -ang

N = int(input())
S = [[int(i) for i in input().split()] for j in range(N)]
T = [[int(i) for i in input().split()] for j in range(N)]

for i in range(N):
    s = translateArr(S, -S[i][0], -S[i][1])
    diss = sorted([distance(0,0,k[0],k[1]) for k in s])
    s.sort(key = lambda x: distance(0,0,x[0],x[1]))
    for j in range(N):
        t = translateArr(T, -T[j][0], -T[j][1])
        # print("-"*10,"\n",s,t)
        dist = sorted([distance(0,0,k[0],k[1]) for k in t])
        if dist != diss:
            continue
        # print("pass")
        ld = dist[-1]
        sa = [i for i in s if distance(0,0,i[0],i[1]) == ld]
        ta = [i for i in t if distance(0,0,i[0],i[1]) == ld]
        for n in sa:
            for m in ta:
                ang = anglefrom(n[0],n[1],m[0],m[1])
                # print("ang between",n,m,ang)
                rs = rotateArr(s, ang)
                # print("rotate",ang,"from",s,"to",rs, sorted(t))
                # print()
                srs = sorted(rs)
                st = sorted(t)
                for i in range(len(srs)):
                    if abs(srs[i][0] - st[i][0]) > 10**-8 or abs(srs[i][1] - st[i][1]) > 10**-8:
                        break
                else:
                    print("Yes")
                    exit()
print("No")