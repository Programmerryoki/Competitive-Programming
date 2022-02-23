from math import acos,asin,atan,pi

vector = lambda a,b: (b[0]-a[0], b[1]-a[1])
dis = lambda x: (x[0]**2 + x[1]**2)**0.5
sine = lambda a,b: (pi + asin((a[0]*b[1]-a[1]*b[0]) / (dis(a)*dis(b))))%pi
cose = lambda a,b: acos((a[0]*b[0]+a[1]*b[1]) / (dis(a)*dis(b)))
tane = lambda a,b: (a[0]*b[1]-a[1]*b[0]) / (a[0]*b[0]+a[1]*b[1])
angle = lambda a,b: pi - cose(a,b)

while True:
    n, *line = [int(i) for i in input().split()]
    if n == 0:
        break
    coor = [[line[i],line[i+1]] for i in range(0,len(line),2)]
    # print(coor)
    angles = [angle(vector(coor[(i-1)%n], coor[i]), vector(coor[i], coor[(i+1)%n])) for i in range(n)]
    # print(angles)
    while True:
        ma = min(angles)
        index = angles.index(ma)
        print(index)
        angs0 = angle(vector(coor[(index-2)%len(coor)], coor[(index-1)%len(coor)]), vector(coor[(index+1)%len(coor)], coor[(index-1)%len(coor)]))
        angs1 = angle(vector(coor[(index-1)%len(coor)], coor[(index+1)%len(coor)]), vector(coor[(index+2)%len(coor)], coor[(index+1)%len(coor)]))
        print([i/(2*pi)*360 for i in angles])
        print(coor[(index-2)%len(coor)], coor[(index-1)%len(coor)], coor[(index)%len(coor)],coor[(index+1)%len(coor)],coor[(index+2)%len(coor)])
        print("\t",ma, angs0, angs1)
        if angs0 < ma or angs1 < ma:
            break

        temp = [coor[i] for i in range(len(coor)) if i != index]
        print(temp)
        tangle = [angle(vector(temp[(i-1)%len(temp)], temp[i]), vector(temp[(i+1)%len(temp)], temp[i])) for i in range(len(temp))]
        coor = temp
        angles = tangle
    print(len(coor)," ".join(" ".join(map(str, i)) for i in coor))