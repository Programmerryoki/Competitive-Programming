T, A, B = [int(i) for i in input().split()]
pos = [[0,0],
       [500000000, 500000000],[-500000000, 500000000],[500000000, -500000000],[-500000000, -500000000],
       [250000000, 250000000],[-250000000, 250000000],[250000000, -250000000],[-250000000, -250000000],
       [750000000, 250000000],[-750000000, 250000000],[750000000, -250000000],[-750000000, -250000000],
       [250000000, 750000000],[-250000000, 750000000],[250000000, -750000000],[-250000000, -750000000],
       [750000000, 750000000],[-750000000, 750000000],[750000000, -750000000],[-750000000, -750000000],
       ]
for case in range(T):
    c = [0,0]
    x = [0,0]
    y = [0,0]
    for a in pos:
        print(a[0], a[1])
        res = input()
        if res == "CENTER" or res == "HIT":
            c = a
            x = [a[0], a[0]]
            y = [a[1], a[1]]
            break

    def binarylx(l, r, other):
        global c,x,y
        if r >= l:
            if abs(r - l) <= 1:
                x[0] = l
                return False
            m = l + (r - l)//2
            print(m,other)
            # print(m, other, l,r)
            res = input()
            if res == "MISS":
                return binarylx(m, r, other)
            elif res == "CENTER":
                c = [m, other]
                return True
            return binarylx(l, m, other)

    def binaryrx(l, r, other):
        global c,x,y
        if r >= l:
            if abs(r - l) <= 1:
                x[1] = r
                return False
            m = l + (r - l)//2
            print(m,other)
            # print(m, other, l,r)
            res = input()
            if res == "MISS":
                return binaryrx(l, m, other)
            elif res == "CENTER":
                c = [m, other]
                return True
            return binaryrx(m, r, other)

    def binaryly(l, r, other):
        global c,x,y
        if r >= l:
            if abs(r - l) <= 1:
                y[0] = l
                return False
            m = l + (r - l)//2
            print(other, m)
            # print(m, other, l,r)
            res = input()
            if res == "MISS":
                return binaryly(m, r, other)
            elif res == "CENTER":
                c = [m, other]
                return True
            return binaryly(l, m, other)

    def binaryry(l, r, other):
        global c,x,y
        if r >= l:
            if abs(r - l) <= 1:
                y[1] = r
                return False
            m = l + (r - l)//2
            print(other, m)
            # print(m, other, l,r)
            res = input()
            if res == "MISS":
                return binaryry(l, m, other)
            elif res == "CENTER":
                c = [m, other]
                return True
            return binaryry(m, r, other)

    if binarylx(-10**9, x[0], y[0]):
        continue
    if binaryrx(x[1], 10**9, y[0]):
        continue
    mx = (x[1] + x[0])//2
    if binaryly(-10**9, y[0], mx):
        continue
    if binaryry(y[1], 10**9, mx):
        continue

    print(mx, (y[0] + y[1])//2)
    res = input()
    if res == "CENTER":
        continue