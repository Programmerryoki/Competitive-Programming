n = int(input())
if n == 0:
    print("0")
else:
    s = [int(i) for i in input().split()]
    if 0 in s:
        print("0")
    else:
        c = 1
        cs = 0
        for a in s:
            m = a%9
            if m != 0:
                c *= m
            else:
                c *= 9
        # print(c)
        # print("mod",c%9)
        print(c%9 if c%9 != 0 else 9)
        # su = sum([int(i) for i in str(c)])
        # while len(str(su)) > 1:
        #     print("su",su)
        #     su = sum([int(i) for i in str(su)])
        # print("ans",su)

        # c = 1
        # cs = 0
        # for a in s:
        #     su = a
        #     while len(str(su)) > 1:
        #         su = sum([int(i) for i in str(su)])
        #     c *= su
        #     print("c",sum([int(i) for i in str(c)]))
        #     cs += su
        # print(c,cs)