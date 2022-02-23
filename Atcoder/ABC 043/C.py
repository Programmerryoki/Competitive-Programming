N = int(input())
A = [int(i) for i in input().split()]
ave = sum(A)//len(A)


def cost(A,ave):
    return sum(map(lambda x: (x - ave)**2, A))


c = cost(A, ave)
c1 = cost(A,ave+1)
if c < c1:
    while c < c1:
        ave -= 1
        c, c1 = cost(A, ave), c
    print(c1)
else:
    while c > c1:
        ave += 1
        c, c1 = c1, cost(A, ave)
    print(c)