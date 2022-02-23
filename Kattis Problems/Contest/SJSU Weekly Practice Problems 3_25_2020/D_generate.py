# hp = [["1"]]
hp = [[1]]
for num in range(6):
    h = [[0]*(len(hp)*2) for i in range(len(hp)*2)]
    for i in range(2):
        for j in range(2):
            for a in range(len(hp)):
                for b in range(len(hp)):
                    if i == j == 1:
                        # h[i*len(hp) + a][j*len(hp) + b] = " "
                        h[i*len(hp) + a][j*len(hp) + b] = -hp[a][b]
                    else:
                        h[i*len(hp) + a][j*len(hp) + b] = hp[a][b]
                        # h[i*len(hp) + a][j*len(hp) + b] = " "
    # print(len(h))
    # for i,a in enumerate(h, 1):
    #     print(str(i) + " :", end = "")
    #     for b in a:
    #         # print("{0:3d}".format(b), end = "")
    #         if b == -1:
    #             print("{0:3d}".format(b), end = "")
    #         else:
    #             print("   ", end = "")
    #     print()
    hp = h
    # print()
    # print(" "*6 + " ".join(map(str, [i for i in range(2**(num+1))])))
    for i,a in enumerate(h):
        print(str(i) + " :", end = "")
        for b in a:
            # print("{0:3d}".format(b), end = "")
            if b == 1:
                print("{0:3d}".format(b), end = "")
            else:
                print("   ", end = "")
        print()
    print()