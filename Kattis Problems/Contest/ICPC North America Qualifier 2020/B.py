from math import pi, sin, cos,tan, asin, acos, atan, degrees

class Circle:
    def __init__(self, x,y,radius):
        self.radius = radius
        self.x = x
        self.y = y
        self.visible = [[0,360]]

    def isOverlapped(self, other):
        return self.distance(other) < self.radius + other.radius

    def cover(self, start, end):
        normal = start < end
        new = []
        for s,e in self.visible:
            if normal and ((start < end < s) or (e < start < end)):
                new.append([s,e])
                continue
            if not normal and (end < s < e < start):
                new.append([s,e])
                continue
            if normal and s <= start < end <= e:
                if s != start:
                    new.append([s,start])
                if end != e:
                    new.append([end,e])
            elif normal and s <= start <= e <= end:
                if s != start:
                    new.append([s,start])
            elif normal and start <= s <= end <= e:
                if end != e:
                    new.append([end, e])
            if not normal and (s <= end < start <= e):
                new.append([end, start])
            elif not normal and s <= start <= e:
                if s != start:
                    new.append([s, start])
            elif not normal and s <= end <= e:
                if end != e:
                    new.append([end, e])
        self.visible = new

    def length(self):
        tl = sum([i[1] - i[0] for i in self.visible] + [0])
        return 2 * pi * tl / 360 * self.radius

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def toString(self):
        return str(self.x) +" "+ str(self.y) +" "+ str(self.radius) +" "+ " ".join(["("+str(i[0])+","+str(i[1])+")" for i in self.visible])

N = int(input())
circs = []
for _ in range(N):
    x,y,r = map(int, input().split())
    cir = Circle(x,y,r)
    for i in circs:
        if not cir.isOverlapped(i):
            continue

        dis = cir.distance(i)
        if cir.radius >= i.radius + dis:
            i.cover(0,360)
            continue

        vecr = [cir.x - i.x, cir.y - i.y]
        try:
            off = atan(abs(vecr[1]) / abs(vecr[0]))
            off = degrees(off)
        except:
            off = 0
        if vecr[0] > 0 and vecr[1] > 0:
            off = 90 - off
        elif vecr[0] > 0 and vecr[1] < 0:
            off += 90
        elif vecr[0] < 0 and vecr[1] < 0:
            off += 180
        elif vecr[0] < 0 and vecr[1] > 0:
            off += 360 - off
        elif vecr[0] == 0:
            off = 0 if vecr[1] > 0 else 180 if vecr[1] < 0 else 0
        elif vecr[1] == 0:
            off = 90 if vecr[0] > 0 else 270 if vecr[0] < 0 else 0

        print()
        print(i.toString(), cir.toString())
        print(dis)
        print(dis / 2, i.radius, (dis/2)/i.radius)
        tmp = dis / 2
        ang = acos(tmp / i.radius)
        ang = degrees(ang)
        angs = [(off - ang + 360)%360, (off + ang)%360]
        print(angs)
        i.cover(angs[0], angs[1])

    circs.append(cir)

total = 0
for i in circs:
    print(i.toString())
    total += i.length()
print(total)