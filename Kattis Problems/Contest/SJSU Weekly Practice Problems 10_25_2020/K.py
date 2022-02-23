T = int(input())
for _ in range(T):
    mi = [float("inf"), float("inf")]
    n = int(input())
    for a in range(1,5*10**5):
        for b in range(a,5*10**5):
            if b > n:
                break
            t = [a,b]
            # print(t)
            while t[1] < n:
                t[0],t[1] = t[1], t[0]+t[1]
            # print("\t",t)
            if mi[1] > t[1]:
                mi = [a,b]
    print(mi)


# # fib = lambda n: round((1 / (5)**0.5) * (((1 + (5)**0.5) / 2)**n - ((1 - (5)**0.5) / 2)**n))
# # gib = lambda n, f: round((f / (5)**0.5) * (((1 + (5)**0.5) / 2)**n - ((1 - (5)**0.5) / 2)**n))
#
# def mm(m1,m2):
#     [a,b],[c,d] = m1
#     [e,f],[g,h] = m2
#     return [[a*e+b*g, a*f+b*h], [c*e+d*g, c*f+d*h]]
#
# fib = [[1,1],[1,0]]
#
# T = int(input())
# n = [[1,1],[1,0]]
# for i in range(T):
#     for j in n:
#         print(j)
#     print()
#     n = mm(n, fib)