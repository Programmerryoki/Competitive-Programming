N = int(input())
while N != 0:
    ppl = [input().split() for i in range(N*2)]
    # for a in ppl:
    #     print(a)
    #     x = int(a[1])
    #     y = int(a[2])
    #     print((x**2 + y**2)**0.5)
    ppl.sort(key = lambda x: (int(x[1])**2 + int(x[2])**2)**0.5)
    for a in ppl:
        print(a)
    print("\n\n")


    N = int(input())