from math import asin, atan, degrees

N = int(input())
for _ in range(N):
    n,d = map(int, input().split())
    trains = []
    notrain = False
    for _ in range(n):
        x,y = map(int, input().split())
        dis = (x**2 + y**2)**0.5
        if dis <= d:
            notrain = True
            continue
        if x == 0 and 0 < y:
            ang = 90
        elif x == 0 and y < 0:
            ang = 270
        elif y == 0 and 0 < x:
            ang = 0
        elif y == 0 and x < 0:
            ang = 180
        elif 0 < x and 0 < y:
            ang = degrees(atan(y / x))
        elif x < 0 and 0 <= y:
            ang = 180 - degrees(atan( y / (-x) ))
        elif x < 0 and y < 0:
            ang = 180 + degrees(atan( (-y) / (-x)))
        else:
            ang = 360 - degrees(atan( (-y) / x ))
        diff = degrees(asin(d / dis))
        ran = [(ang - diff)%360, (ang + diff)%360]
        if diff >= 180:
            ran = [0,360]

        connect = []
        for i,[da,db] in enumerate(trains):
            if ran[-1] < da or ran[0] > db:
                continue
            else:
                trains[i] = [min(da, ran[0]), max(db, ran[1])]
                break
        else:
            trains.append(ran)
    print(len(trains)+(notrain and not len(trains)))